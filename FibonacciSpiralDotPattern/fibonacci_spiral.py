r"""
環境配置:
 1. 建立虛擬環境: python -m venv venv
 2. 啟動虛擬環境: .\venv\Scripts\activate (Windows) 或 source venv/bin/activate (Mac/Linux)
 3. 安裝相依庫: pip install numpy matplotlib ezdxf packaging sv-ttk
 4. 執行程式: python fibonacci_spiral_v4.py
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors # 引入顏色向量化處理
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys

# --- 依賴項檢查 ---
try:
    import ezdxf
except ModuleNotFoundError:
    print("錯誤: 缺少 `ezdxf`。請執行 `pip install ezdxf`。")
    sys.exit()

try:
    import sv_ttk
except ModuleNotFoundError:
    print("錯誤: 缺少 `sv_ttk`。請執行 `pip install sv-ttk`。")
    sys.exit()

# ==============================================================================
#  可重用的 UI 元件類別
# ==============================================================================
class AdjustmentPanel(ttk.Frame):
    """微調面板：負責數值輸入與滑桿控制"""
    def __init__(self, parent, text, variable, from_, to, resolution, reset_value, update_callback, deltas=None):
        super().__init__(parent)
        self.variable = variable
        self.update_callback = update_callback
        self.reset_value = reset_value
        
        self.columnconfigure(1, weight=1)

        # 標題與輸入框
        top_frame = ttk.Frame(self)
        top_frame.pack(fill="x", pady=(0, 2))
        ttk.Label(top_frame, text=text, font=("Segoe UI", 9, "bold")).pack(side="left")
        
        self.entry = ttk.Entry(top_frame, textvariable=self.variable, width=10, justify="right")
        self.entry.pack(side="right")
        self.entry.bind("<Return>", lambda e: self.update_callback())
        # 增加 FocusOut 事件，確保滑鼠點開時也更新
        self.entry.bind("<FocusOut>", lambda e: self.update_callback())

        # 滑桿
        slider = ttk.Scale(self, from_=from_, to=to, orient=tk.HORIZONTAL, variable=self.variable, command=lambda v: self.update_callback())
        slider.pack(fill="x", pady=(0, 5))

        # 控制按鈕
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x")
        # 動態權重配置
        total_cols = len(deltas) + 1 if deltas else 5
        btn_frame.columnconfigure(list(range(total_cols)), weight=1)

        if deltas is None:
            deltas = [("⏪", -1.0), ("◀", -0.1), ("▶", 0.1), ("⏩", 1.0)]

        for i, (icon, delta) in enumerate(deltas):
            btn = ttk.Button(btn_frame, text=icon, width=3, 
                           command=lambda d=delta: self.adjust_value(d))
            btn.grid(row=0, column=i, padx=1, sticky="ew")

        # 重設按鈕
        ttk.Button(btn_frame, text="↺", width=3, 
                   command=self.do_reset).grid(row=0, column=len(deltas), padx=1, sticky="ew")

    def adjust_value(self, delta):
        try:
            current = float(self.variable.get())
            new_val = current + delta
            # 智慧格式化
            if abs(delta) < 0.01:
                self.variable.set(f"{new_val:.4f}")
            elif abs(delta) < 1:
                self.variable.set(f"{new_val:.2f}")
            else:
                self.variable.set(f"{new_val:.1f}")
            self.update_callback()
        except ValueError:
            self.do_reset()

    def do_reset(self):
        self.variable.set(self.reset_value)
        self.update_callback()

# ==============================================================================
#  主應用程式類別
# ==============================================================================
class PhyllotaxisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --- 1. 初始化設定 ---
        self.title("Fibonacci Generator v4.0 by lee18.in")
        self.geometry("1100x900")
        
        plt.style.use('dark_background')
        sv_ttk.set_theme("dark")

        # --- 2. 核心變數 ---
        self.all_black_mode = False
        self.export_data = {'x': [], 'y': [], 'sizes': [], 'colors': []} # 用字典儲存完整數據
        self._draw_job = None
        
        self._init_variables()
        self._init_ui()
        self._bind_events()
        
        # 初始繪圖
        self.request_update()

    def _init_variables(self):
        """初始化 Tkinter 變數"""
        self.num_points_var = tk.IntVar(value=1000)
        self.point_size_var = tk.DoubleVar(value=10.0) # 改為 Double 以支援細微調整
        self.radius_func_var = tk.StringVar(value="n ^ 0.x")
        self.exponent_var = tk.DoubleVar(value=0.5)
        self.fib_del_batches_var = tk.IntVar(value=0)
        self.density_var = tk.StringVar(value="標準")
        self.growth_factor_var = tk.DoubleVar(value=0.0)
        self.radius_scale_var = tk.DoubleVar(value=1.0)
        self.shape_var = tk.StringVar(value="圓形")
        self.angle_adjust_var = tk.DoubleVar(value=0.0)
        self.hue_delta_var = tk.DoubleVar(value=137.507764)
        self.size_gradient_var = tk.DoubleVar(value=0.0)

    def _init_ui(self):
        """建立 UI 佈局"""
        self.columnconfigure(0, weight=0, minsize=380)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # 左側控制區
        self.control_container = ttk.Frame(self, padding=15)
        self.control_container.grid(row=0, column=0, sticky="nsew")
        
        # 右側繪圖區
        self.plot_frame = ttk.Frame(self)
        self.plot_frame.grid(row=0, column=1, sticky="nsew")

        # 標題
        ttk.Label(self.control_container, text="Fibonacci Engineering", font=("Segoe UI", 20, "bold")).pack(anchor="w", pady=(0, 10))

        # 頁籤
        notebook = ttk.Notebook(self.control_container)
        notebook.pack(fill="both", expand=True)

        self.tab_main = ttk.Frame(notebook, padding=10)
        self.tab_fine_tune = ttk.Frame(notebook, padding=10)
        
        notebook.add(self.tab_main, text='⚙️ 參數')
        notebook.add(self.tab_fine_tune, text='🎛️ 微調')

        self._build_main_tab()
        self._build_finetune_tab()
        self._build_footer_buttons()
        self._build_plot_area()

    def _build_main_tab(self):
        # 幾何參數
        group_geo = ttk.LabelFrame(self.tab_main, text="幾何參數 (Geometry)", padding=10)
        group_geo.pack(fill="x", pady=5)
        group_geo.columnconfigure(1, weight=1)

        controls = [
            ("點的總數 (N):", ttk.Spinbox(group_geo, textvariable=self.num_points_var, from_=100, to=50000, increment=100)),
            ("基礎大小 (Size):", ttk.Spinbox(group_geo, textvariable=self.point_size_var, from_=1, to=200, increment=1)),
            ("形狀 (Shape):", ttk.Combobox(group_geo, textvariable=self.shape_var, values=["圓形", "正六邊形"], state='readonly')),
            ("數學模型:", ttk.Combobox(group_geo, textvariable=self.radius_func_var, values=["n ^ 0.x", "log(n)", "sqrt(n)"], state='readonly')),
            ("密度修正:", ttk.Combobox(group_geo, textvariable=self.density_var, values=["標準", "均衡密度"], state='readonly'))
        ]

        for idx, (label_text, widget) in enumerate(controls):
            ttk.Label(group_geo, text=label_text).grid(row=idx, column=0, sticky="w", pady=5)
            widget.grid(row=idx, column=1, sticky="ew", padx=5)

    def _build_finetune_tab(self):
        # 使用封裝好的 AdjustmentPanel
        params = [
            ("大小漸變 (Size Grad):", self.size_gradient_var, 0.0, 50, 0.1, 0.0, [("⏪",-0.5), ("◀",-0.1), ("▶",0.1), ("⏩",0.5)]),
            ("角度偏移 (Angle):", self.angle_adjust_var, -720, 720, 0.01, 0.0, [("⏪",-10), ("◀",-0.1), ("▶",0.1), ("⏩",10)]),
            ("色相增量 (Hue):", self.hue_delta_var, 0, 360, 0.1, 137.507764, [("⏪",-10), ("◀",-0.5), ("▶",0.5), ("⏩",10)]),
            ("指數 (Power):", self.exponent_var, 0.1, 1.0, 0.01, 0.5, [("◀",-0.05), ("▶",0.05)]),
            ("縮放 (Scale):", self.radius_scale_var, 0.1, 5.0, 0.1, 1.0, None),
            ("非線性成長 (Growth):", self.growth_factor_var, -2.0, 2.0, 0.1, 0.0, None),
            ("Fibonacci 刪除:", self.fib_del_batches_var, 0, 25, 1, 0, [("-",-1), ("+",1)])
        ]

        for label, var, f, t, res, rst, deltas in params:
            panel = AdjustmentPanel(self.tab_fine_tune, label, var, f, t, res, rst, self.request_update, deltas)
            panel.pack(fill="x", pady=5)

    def _build_footer_buttons(self):
        btn_container = ttk.Frame(self.control_container)
        btn_container.pack(side="bottom", fill="x", pady=10)
        
        ttk.Button(btn_container, text="🔄 立即重繪", style="Accent.TButton", command=self.perform_update).pack(fill="x", pady=2)
        
        grid_btn = ttk.Frame(btn_container)
        grid_btn.pack(fill="x", pady=2)
        grid_btn.columnconfigure((0,1,2), weight=1)
        
        ttk.Button(grid_btn, text="👁️ 高對比", command=self.toggle_all_black).grid(row=0, column=0, sticky="ew", padx=1)
        ttk.Button(grid_btn, text="🎨 彩色", command=self.reset_black_mode).grid(row=0, column=1, sticky="ew", padx=1)
        ttk.Button(grid_btn, text="💾 匯出工程圖", command=self.export_file).grid(row=0, column=2, sticky="ew", padx=1)

    def _build_plot_area(self):
        # 這裡設定 Figure 大小，dpi=100 確保在不同解析度螢幕上有基本可讀性
        self.fig, self.ax = plt.subplots(figsize=(6, 6), dpi=100)
        self.fig.patch.set_facecolor('#1c1c1c')
        self.ax.set_facecolor('#1c1c1c')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def _bind_events(self):
        variables = [
            self.num_points_var, self.point_size_var, self.radius_func_var, 
            self.density_var, self.shape_var, self.angle_adjust_var,
            self.hue_delta_var, self.exponent_var, self.radius_scale_var,
            self.growth_factor_var, self.fib_del_batches_var,
            self.size_gradient_var
        ]
        for var in variables:
            var.trace_add("write", lambda *args: self.request_update())

    # ==========================================================================
    #  核心邏輯 (Core Logic)
    # ==========================================================================
    
    def request_update(self, *args):
        if self._draw_job:
            self.after_cancel(self._draw_job)
        self._draw_job = self.after(50, self.perform_update) # 50ms 反應更快

    def perform_update(self):
        try:
            # 1. 參數讀取
            N = self.num_points_var.get()
            base_size = self.point_size_var.get()
            radius_func = self.radius_func_var.get()
            density_mode = self.density_var.get()
            angle_adj = self.angle_adjust_var.get()
            scale = self.radius_scale_var.get()
            growth = self.growth_factor_var.get()
            hue_delta = self.hue_delta_var.get()
            fib_batches = self.fib_del_batches_var.get()
            marker = "o" if self.shape_var.get() == "圓形" else "h"
            exponent = self.exponent_var.get()
            size_grad = self.size_gradient_var.get()

            # 2. NumPy 向量化運算 (加速核心) 🚀
            indices = np.arange(1, N + 1, dtype=np.float64) # 使用 float64 避免溢位
            
            # 半徑計算
            effective_exponent = exponent * scale
            if radius_func == "n ^ 0.x":
                r = indices ** effective_exponent
            elif radius_func == "log(n)":
                r = np.log1p(indices) * scale
            else: # sqrt(n)
                r = indices ** (0.5 * scale)
            
            if density_mode == "均衡密度":
                r = r / np.sqrt(N) * np.sqrt(indices)

            # 非線性成長
            if abs(growth) > 0.001:
                r *= (1 + growth / (indices + 1))

            # 角度計算
            golden_angle = np.pi * (3. - np.sqrt(5.))
            theta = indices * (golden_angle + np.radians(angle_adj) / np.log1p(indices))

            x_vals = r * np.cos(theta)
            y_vals = r * np.sin(theta)

            # 大小漸變計算 (Base Size * Gradient Factor)
            # 正規化索引 0~1
            norm_indices = indices / N
            sizes = base_size * (1 + size_grad * norm_indices)

            # 3. 顏色計算 (向量化) 🚀
            if self.all_black_mode:
                colors = np.array([[1, 1, 1, 1]]) # White RGBA
            else:
                hue = ((indices - 1) * hue_delta) % 360 / 360.0
                # 建立 HSV 陣列: [H, S, V]
                # Saturation = 0.8, Value = 1.0
                hsv = np.column_stack((hue, np.full_like(hue, 0.8), np.full_like(hue, 1.0)))
                colors = mcolors.hsv_to_rgb(hsv) # C-level conversion

            # 4. Fibonacci 批次刪除
            if fib_batches > 0:
                delete_count = self._get_fib_sum(int(fib_batches))
                if delete_count < N:
                    x_vals = x_vals[delete_count:]
                    y_vals = y_vals[delete_count:]
                    sizes = sizes[delete_count:]
                    if not self.all_black_mode:
                        colors = colors[delete_count:]
            
            # 儲存數據供匯出
            self.export_data = {
                'x': x_vals,
                'y': y_vals,
                'sizes': sizes,
                'colors': colors,
                'marker': marker
            }

            # 5. 繪圖
            self.ax.clear()
            self.ax.scatter(x_vals, y_vals, s=sizes, c=colors, marker=marker, alpha=0.9, linewidths=0)
            self.ax.set_aspect('equal', adjustable='box')
            self.ax.axis("off")
            self.fig.tight_layout(pad=0)
            self.canvas.draw()

        except Exception as e:
            print(f"Update Error: {e}") # 捕捉錯誤但不崩潰

    def _get_fib_sum(self, n):
        # 快速計算前 n 項 Fibonacci 總和
        if n <= 0: return 0
        a, b = 1, 1
        total = 0
        for _ in range(n):
            total += a
            a, b = b, a + b
        return total

    def toggle_all_black(self):
        self.all_black_mode = True
        self.request_update()

    def reset_black_mode(self):
        self.all_black_mode = False
        self.request_update()

    # ==========================================================================
    #  匯出功能 (Export)
    # ==========================================================================
    def export_dxf(self, filepath, data, as_circles=True):
        """匯出 DXF，支援實體圓"""
        try:
            doc = ezdxf.new(dxfversion="R2010")
            msp = doc.modelspace()
            
            x = data['x']
            y = data['y']
            sizes = data['sizes']
            
            # Matplotlib 的 s 是 "點的面積 (points^2)"
            # 我們需要轉換成 DXF 的半徑。這是一個視覺近似。
            # 假設 DPI=72 (Matplotlib 預設), 1 point = 1/72 inch.
            # 這裡簡化：取 sqrt(size) 並乘以一個比例因子讓 CAD 看起來合理
            # 實際上工程師通常希望指定真實物理半徑，這裡先做視覺對應。
            radii = np.sqrt(sizes) * 0.05 

            print(f"Exporting {len(x)} entities to DXF...")

            if as_circles:
                for i in range(len(x)):
                    msp.add_circle((x[i], y[i]), radius=radii[i])
            else:
                for i in range(len(x)):
                    msp.add_point((x[i], y[i]))

            doc.saveas(filepath)
            messagebox.showinfo("匯出成功", f"DXF (R2010) 已儲存。\n實體類型: {'Circle' if as_circles else 'Point'}\n路徑: {filepath}")
        except Exception as e:
            messagebox.showerror("匯出失敗", str(e))

    def export_file(self):
        filetypes = [
            ("PNG 影像", "*.png"), 
            ("SVG 向量圖", "*.svg"), 
            ("DXF (圓形實體)", "*.dxf"), 
            ("DXF (純點)", "*.dxf")
        ]
        # 自定義對話框行為
        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=filetypes)
        if not filepath: return
        
        ext = os.path.splitext(filepath)[1].lower()
        
        if ext == ".dxf":
            # 判斷使用者選了哪種 DXF 模式 (簡易判斷)
            # 在 filedialog 中無法直接獲取 filter index，這裡我們做一個簡單的詢問
            use_circles = messagebox.askyesno("DXF 設定", "是否匯出為「圓形實體 (Circle)」以保留大小資訊？\n\n(No = 匯出為純點)")
            self.export_dxf(filepath, self.export_data, as_circles=use_circles)
        else:
            # 圖片匯出
            try:
                self.fig.patch.set_alpha(0) 
                self.ax.patch.set_alpha(0)
                self.fig.savefig(filepath, bbox_inches='tight', pad_inches=0.1, dpi=300, transparent=True)
                self.fig.patch.set_alpha(1)
                self.ax.patch.set_alpha(1)
                messagebox.showinfo("成功", f"圖檔已儲存: {filepath}")
            except Exception as e:
                messagebox.showerror("錯誤", str(e))

if __name__ == "__main__":
    app = PhyllotaxisApp()
    app.mainloop()