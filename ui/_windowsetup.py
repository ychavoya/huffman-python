from tkinter import Label, Button, Message, Entry, Scrollbar, font
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror
from tkinter.ttk import Notebook, Frame
import tkinter as tk
from ui.scrollframe import VScrollFrame

charwidth = 600

class MainWindow(tk.Frame):
    
    def __init__(self, title, compress_fn, decompress_fn):
        tk.Frame.__init__(self)
        root = self.master
        root.title()
        root.geometry(f'{charwidth + 150}x400')

        self.bold_font = font.Font(family='TkTextFont', size=10, weight='bold')

        # =================================

        tab_root = Notebook(root)

        tab_compress = VScrollFrame(tab_root)
        tab_decompress = VScrollFrame(tab_root)

        tab_root.add(tab_compress, text='Comprimir')
        tab_root.add(tab_decompress, text='Descomprimir')

        tab_root.pack(expand=1, fill=tk.BOTH)
        tab_cmp_root = tab_compress.interior
        tab_dcp_root = tab_decompress.interior

        # =================================

        self.cmd_compress = compress_fn
        self.cmd_decompress = decompress_fn

        self._setup_cmp(tab_cmp_root)
        self._setup_dcp(tab_dcp_root)

        # =================================

    def clipboard_copy(self, target):
        cb = tk.Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(target)
        cb.update()
        cb.destroy()

    def _setup_cmp(self, tab_cmp_root):

        row = 0

        tk.Label(tab_cmp_root, text='Texto a comprimir:', font=self.bold_font).grid(row=row, column=0, pady=10, padx=10, sticky=tk.W)

        row += 1

        self.original_entry = ScrolledText(tab_cmp_root, width=50, height=6, wrap=tk.WORD)
        self.original_entry.grid(row=row, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W+tk.E)

        self.btn_1 = tk.Button(tab_cmp_root, text="Comprimir", command=self.cmd_compress)
        self.btn_1.grid(row=row, column=2, pady=10, padx=10, sticky=tk.N)

        # =================================

        row += 1

        (tk.Label(tab_cmp_root, text='Texto comprimido en binario:', font=self.bold_font)
            .grid(row=row, column=0, columnspan=2, padx=10, sticky='sw'))

        row += 1

        self.strv_compressed = tk.StringVar()
        (tk.Message(tab_cmp_root, width=charwidth, justify='left', textvariable=self.strv_compressed,relief='groove')
            .grid(row=row,pady=10,padx=10,column=0, columnspan=2, sticky='w'))

        tk.Button(tab_cmp_root, text="Copiar", command=self.btn_cp_cmp).grid(row=row,padx=10,column=2, sticky=tk.N)

        # =================================

        row += 1
        
        tk.Label(tab_cmp_root, text='Código para descomprimir:', font=self.bold_font).grid(row=row, column=0, columnspan=2, padx=10, sticky=tk.S+tk.W)

        row += 1

        self.strv_encoded = tk.StringVar()
        (tk.Message(tab_cmp_root, width=charwidth, justify='left', textvariable=self.strv_encoded,relief='groove')
            .grid(row=row,pady=10,padx=10,column=0, columnspan=2, sticky=tk.W))

        tk.Button(tab_cmp_root, text="Copiar", command=self.btn_cp_cod).grid(row=row,padx=10,column=2, sticky=tk.N)

        # =================================

        row += 1

        self.strv_rate = tk.StringVar()
        tk.Label(tab_cmp_root, textvariable=self.strv_rate,font=self.bold_font).grid(row=row, column=0, columnspan=3, padx=10, sticky=tk.S+tk.W)

        # =================================

        tab_cmp_root.grid_columnconfigure(1, weight=1)
        tab_cmp_root.grid_rowconfigure(1, weight=1)
        tab_cmp_root.grid_rowconfigure(3, weight=1)
        tab_cmp_root.grid_rowconfigure(5, weight=1)

        # =================================

    def _setup_dcp(self, tab_dcp_root):

        row = 0

        tk.Label(tab_dcp_root, text='Texto a descomprimir:', font=self.bold_font).grid(row=row, column=0, pady=10, padx=10, sticky=tk.W)
        
        self.btn_2 = tk.Button(tab_dcp_root, text="Descomprimir", command=self.cmd_decompress)
        self.btn_2.grid(row=1, column=2, pady=10, padx=10, rowspan=4, sticky=tk.S)

        row += 1

        self.decompress_entry = ScrolledText(tab_dcp_root, width=50, height=6, wrap=tk.CHAR)
        self.decompress_entry.grid(row=row, column=0, columnspan=2, sticky=tk.W+tk.E)

        row += 1

        tk.Label(tab_dcp_root, text='Código para descomprimir:', font=self.bold_font).grid(row=row, column=0, pady=10, padx=10, sticky=tk.W)

        row += 1

        self.code_entry = ScrolledText(tab_dcp_root, width=50, height=6, wrap=tk.CHAR)
        self.code_entry.grid(row=row, column=0, columnspan=2, sticky=tk.W+tk.E)

        # =================================

        row += 1

        tk.Label(tab_dcp_root, text="Texto original:", font=self.bold_font).grid(row=row, column=0, columnspan=2, padx=10, pady=0, sticky=tk.SW)

        row += 1

        self.strv_original2 = tk.StringVar()
        (tk.Message(tab_dcp_root, width=charwidth, justify='left', textvariable=self.strv_original2, relief='groove')
            .grid(row=row, pady=10, padx=10, column=0, columnspan=2, sticky='w'))

        tk.Button(tab_dcp_root, text="Copiar", command=self.btn_cp_ori).grid(row=row,padx=10,column=2, sticky=tk.N)

         # =================================

        tab_dcp_root.grid_columnconfigure(1, weight=1)
        tab_dcp_root.grid_rowconfigure(row, weight=1)

        # =================================

    def btn_cp_cmp(self):
        self.clipboard_copy(self.strv_compressed.get())
    
    def btn_cp_cod(self):
        self.clipboard_copy(self.strv_encoded.get())
        
    def btn_cp_ori(self):
        self.clipboard_copy(self.strv_original2.get())