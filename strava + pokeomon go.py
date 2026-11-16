import tkinter as tk
from tkinter import messagebox
import random

class UnejQuestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UNEJ Quest: Walk & Hydrate")
        self.root.geometry("450x650")
        self.root.configure(bg="#1b5e20") # Nuansa hijau kampus UNEJ
        self.root.resizable(False, False)

        # Variabel Game
        self.distance = 0.0  # dalam km
        self.rewards = 0
        self.is_moving = False
        self.pet_mood = "💤 Haus (Mulai bergerak di sekitar UNEJ!)"
        
        self.setup_ui()

    def setup_ui(self):
        # Header / Judul Game
        header_frame = tk.Frame(self.root, bg="#1b5e20")
        header_frame.pack(pady=15)

        title_label = tk.Label(
            header_frame, 
            text="🌿 UNEJ QUEST: HYDRA-RUN 💧", 
            font=("Helvetica", 16, "bold"), 
            bg="#1b5e20", 
            fg="#81c784"
        )
        title_label.pack()

        self.status_label = tk.Label(
            header_frame, 
            text=self.pet_mood, 
            font=("Helvetica", 10, "italic"), 
            bg="#1b5e20", 
            fg="#ffffff"
        )
        self.status_label.pack(pady=5)

        # Simulasi Peta Area UNEJ (Canvas)
        map_frame = tk.Frame(self.root, bg="#2e7d32", bd=3, relief=tk.RIDGE)
        map_frame.pack(pady=10)

        self.canvas = tk.Canvas(map_frame, width=400, height=220, bg="#c8e6c9")
        self.canvas.pack()
        
        # Gambar elemen peta mini UNEJ
        self.draw_unej_map()

        # Statistik Game (Jarak & Kupon)
        stats_frame = tk.Frame(self.root, bg="#1b5e20")
        stats_frame.pack(pady=15)

        # Kotak Jarak
        dist_box = tk.Frame(stats_frame, bg="#2e7d32", padx=15, pady=10)
        dist_box.grid(row=0, column=0, padx=10)
        tk.Label(dist_box, text="Jarak Tempuh", font=("Helvetica", 9), bg="#2e7d32", fg="#c8e6c9").pack()
        self.dist_val_label = tk.Label(dist_box, text="0.00 / 1.0 km", font=("Helvetica", 14, "bold"), bg="#2e7d32", fg="#ffffff")
        self.dist_val_label.pack()

        # Kotak Kupon Air
        reward_box = tk.Frame(stats_frame, bg="#2e7d32", padx=15, pady=10)
        reward_box.grid(row=0, column=1, padx=10)
        tk.Label(reward_box, text="Kupon Air Mineral", font=("Helvetica", 9), bg="#2e7d32", fg="#c8e6c9").pack()
        self.reward_val_label = tk.Label(reward_box, text="💧 0 Botol", font=("Helvetica", 14, "bold"), bg="#2e7d32", fg="#ffffff")
        self.reward_val_label.pack()

        # Tombol Aksi Kontrol Game
        control_frame = tk.Frame(self.root, bg="#1b5e20")
        control_frame.pack(pady=10)

        self.btn_move = tk.Button(
            control_frame, 
            text="🚀 Mulai Jalan/Lari di UNEJ", 
            font=("Helvetica", 12, "bold"), 
            bg="#ffb300", 
            fg="#000000", 
            padx=20, 
            pady=10, 
            command=self.toggle_movement
        )
        self.btn_move.pack(pady=5)

        # Info Toko Mitra
        info_label = tk.Label(
            self.root, 
            text="📍 Tukarkan kupon di Kantin Tegal Boto / Perpus UNEJ", 
            font=("Helvetica", 9), 
            bg="#1b5e20", 
            fg="#a5d6a7"
        )
        info_label.pack(side=tk.BOTTOM, pady=15)

    def draw_unej_map(self):
        # Ilustrasi rute dan landmark kampus UNEJ di Canvas
        self.canvas.create_rectangle(20, 20, 380, 200, outline="#1b5e20", width=2, fill="#e8f5e9")
        # Jalan Kampus
        self.canvas.create_line(50, 110, 350, 110, fill="#8d6e63", width=8, dash=(4, 2))
        # Landmark
        self.canvas.create_oval(60, 95, 90, 125, fill="#1976d2")
        self.canvas.create_text(75, 80, text="Rektorat", font=("Helvetica", 8, "bold"), fill="#0d47a1")

        self.canvas.create_oval(180, 95, 210, 125, fill="#388e3c")
        self.canvas.create_text(195, 80, text="Perpus", font=("Helvetica", 8, "bold"), fill="#1b5e20")

        self.canvas.create_oval(300, 95, 330, 125, fill="#e65100")
        self.canvas.create_text(315, 80, text="Kantin Mitra", font=("Helvetica", 8, "bold"), fill="#bf360c")

        # Avatar Pemain (HydroMon/User)
        self.player_icon = self.canvas.create_oval(65, 100, 85, 120, fill="#ffeb3b", outline="#f57f17", width=2)

    def toggle_movement(self):
        if not self.is_moving:
            self.is_moving = True
            self.btn_move.config(text="⏹ Jeda / Berhenti", bg="#e53935", fg="#ffffff")
            self.status_label.config(text="🏃‍♂️ Sedang bergerak menyusuri area kampus UNEJ...")
            self.simulate_progress()
        else:
            self.is_moving = False
            self.btn_move.config(text="🚀 Mulai Jalan/Lari di UNEJ", bg="#ffb300", fg="#000000")
            self.status_label.config(text="⏸ Pelacakan dijeda.")

    def simulate_progress(self):
        if self.is_moving:
            self.distance += 0.25 # Tambah 250 meter per detik simulasi
            
            # Pindahkan posisi ikon pemain di canvas secara visual
            current_coords = self.canvas.coords(self.player_icon)
            if current_coords[0] < 310:
                self.canvas.move(self.player_icon, 70, 0)
            else:
                # Reset posisi ke awal jika sampai ujung
                self.canvas.coords(self.player_icon, 65, 100, 85, 120)

            if self.distance >= 1.0:
                self.distance = 0.0
                self.rewards += 1
                self.dist_val_label.config(text=f"{self.distance:.2f} / 1.0 km")
                self.reward_val_label.config(text=f"💧 {self.rewards} Botol")
                
                self.is_moving = False
                self.btn_move.config(text="🚀 Mulai Jalan/Lari di UNEJ", bg="#ffb300", fg="#000000")
                self.status_label.config(text="🎉 Hore! Kupon Air Mineral Berhasil Didapat!")
                
                # Munculkan pop-up reward
                coupon_code = f"UNEJ-HYDRA-{random.randint(1000, 9999)}"
                messagebox.showinfo(
                    "Selamat! 🎉", 
                    f"Anda berhasil mencapai 1 KM di area UNEJ!\n\nKupon Air Mineral Anda:\nKODE: {coupon_code}\nTunjukkan kode ini ke kasir Kantin Mitra UNEJ terdekat."
                )
                return

            self.dist_val_label.config(text=f"{self.distance:.2f} / 1.0 km")
            # Lanjutkan simulasi setiap 1000ms (1 detik)
            self.root.after(1000, self.simulate_progress)

if __name__ == "__main__":
    root = tk.Tk()
    app = UnejQuestApp(root)
    root.mainloop()