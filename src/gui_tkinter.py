#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developer: Goncalo Bejinha
import Tkinter
import tkMessageBox
import active
import FirewallData
import lan_scan

top = Tkinter.Tk()
top.title("LPD 2015")
#as widgets

def LPDInfo():
	tkMessageBox.showinfo("LPD Aplication", "No âmbito da disciplina de Linguagens de Programação Dinâmica do Mestrado em Engenharia de Segurança Informática foi desenvolvida a presente aplicação, que permite detetar os portos ativos nas máquinas de uma rede local, analisar ficheiros log e salvar relatórios dos dados")

B_info = Tkinter.Button(top, text = "SOBRE A APLICAÇÃO", command = LPDInfo)
Area = Tkinter.Canvas(top, height=150, width=150)
B_nmap = Tkinter.Button( text = "2 - Portos ativos", command = active.main, width=100)
B_mapa = Tkinter.Button( text = "3 - Firewall", command = FirewallData, width=100)
B_lan = Tkinter.Button( text = "1 - IP Scan", command = lan_scan.print_usage, width=100)

B_info.pack()
B_lan.pack()
B_nmap.pack()
B_mapa.pack()



Area.pack()
top.mainloop()


