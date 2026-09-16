# -*- coding: utf-8 -*-
"""EME - LogicAlgo — point d'entree de l'application."""

import tkinter as tk
from app import LogicAlgoApp, resource_path

if __name__ == '__main__':
    root = tk.Tk()
    try:
        _icon = tk.PhotoImage(file=resource_path('resources/LogoEME.png'))
        root.iconphoto(True, _icon)
    except Exception:
        pass
    app = LogicAlgoApp(root)
    root.mainloop()
