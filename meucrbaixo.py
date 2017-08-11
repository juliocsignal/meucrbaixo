#-*- coding:utf-8 -*-

import tkinter

class minhaApp_tk(tkinter.Tk):
    def __init__(self, parent):

        tkinter.Tk.__init__(self, parent)

        self.parent = parent

        self.initialize()


    def initialize(self):

        self.grid()

        #Onde as coisas vão aparecer!

        self.labelDiscip = tkinter.Label(self, text="Disciplinas")
        self.labelDiscip.grid(column=0, row=1, sticky="EW")

        self.labelNota1 = tkinter.Label(self, text="Nota 1")
        self.labelNota1.grid(column=2, row=1, sticky="EW")

        self.labelNota2 = tkinter.Label(self, text="Nota 2")
        self.labelNota2.grid(column=4, row=1, sticky="EW")

        self.labelNota3 = tkinter.Label(self, text="Nota 3")
        self.labelNota3.grid(column=6, row=1, sticky="EW")

        self.labelMedia = tkinter.Label(self, text="Média")
        self.labelMedia.grid(column=8, row=1, sticky="EW")

        self.labelAdmSI = tkinter.Label(self, text="Adm. de Sist. de Informação")
        self.labelAdmSI.grid(column=0, row=3, sticky="EW")

        self.labelAdmEst = tkinter.Label(self, text="Adm. Estratégica")
        self.labelAdmEst.grid(column=0, row=2, sticky="EW")

        self.labelCalc = tkinter.Label(self, text="Cálculo I")
        self.labelCalc.grid(column=0, row=4, sticky="EW")

        self.labelLPII = tkinter.Label(self, text="Ling. de Programação II")
        self.labelLPII.grid(column=0, row=6, sticky="EW")

        self.labelWeb0 = tkinter.Label(self, text="Introdução a Sist. Web")
        self.labelWeb0.grid(column=0, row=5, sticky="EW")

        self.labelPsico = tkinter.Label(self, text="Psicologia Aplicada a SI")
        self.labelPsico.grid(column=0, row=7, sticky="EW")

        self.entryAdmSI1 = tkinter.Entry(self)
        self.entryAdmSI1.grid(column=2,row=3,sticky="EW")

        self.entryAdmSI2 = tkinter.Entry(self)
        self.entryAdmSI2.grid(column=4, row=3, sticky="EW")

        self.entryAdmSI3 = tkinter.Entry(self)
        self.entryAdmSI3.grid(column=6, row=3, sticky="EW")

        self.entryAdmSIMed = tkinter.Entry(self)
        self.entryAdmSIMed.grid(column=8, row=3, sticky="EW")

        self.entryAdmEst1 = tkinter.Entry(self)
        self.entryAdmEst1.grid(column=2, row=2, sticky="EW")

        self.entryAdmEst2 = tkinter.Entry(self)
        self.entryAdmEst2.grid(column=4, row=2, sticky="EW")

        self.entryAdmEst3 = tkinter.Entry(self)
        self.entryAdmEst3.grid(column=6, row=2, sticky="EW")

        self.entryAdmEstMed = tkinter.Entry(self)
        self.entryAdmEstMed.grid(column=8, row=2, sticky="EW")

        self.entryCalc1 = tkinter.Entry(self)
        self.entryCalc1.grid(column=2, row=4, sticky="EW")

        self.entryCalc2 = tkinter.Entry(self)
        self.entryCalc2.grid(column=4, row=4, sticky="EW")

        self.entryCalc3 = tkinter.Entry(self)
        self.entryCalc3.grid(column=6, row=4, sticky="EW")

        self.entryCalcMed = tkinter.Entry(self)
        self.entryCalcMed.grid(column=8, row=4, sticky="EW")

        self.entryLPII1 = tkinter.Entry(self)
        self.entryLPII1.grid(column=2, row=5, sticky="EW")

        self.entryLPII2 = tkinter.Entry(self)
        self.entryLPII2.grid(column=4, row=5, sticky="EW")

        self.entryLPII3 = tkinter.Entry(self)
        self.entryLPII3.grid(column=6, row=5, sticky="EW")

        self.entryLPIIMed = tkinter.Entry(self)
        self.entryLPIIMed.grid(column=8, row=5, sticky="EW")

        self.entryWeb01 = tkinter.Entry(self)
        self.entryWeb01.grid(column=2, row=6, sticky="EW")

        self.entryWeb02 = tkinter.Entry(self)
        self.entryWeb02.grid(column=4, row=6, sticky="EW")

        self.entryWeb03 = tkinter.Entry(self)
        self.entryWeb03.grid(column=6, row=6, sticky="EW")

        self.entryWeb0Med = tkinter.Entry(self)
        self.entryWeb0Med.grid(column=8, row=6, sticky="EW")

        self.entryPsico1 = tkinter.Entry(self)
        self.entryPsico1.grid(column=2, row=7, sticky="EW")

        self.entryPsico2 = tkinter.Entry(self)
        self.entryPsico2.grid(column=4, row=7, sticky="EW")

        self.entryPsico3 = tkinter.Entry(self)
        self.entryPsico3.grid(column=6, row=7, sticky="EW")

        self.entryPsicoMed = tkinter.Entry(self)
        self.entryPsicoMed.grid(column=8, row=7, sticky="EW")

        self.botaoSee = tkinter.Button(self, text="Calcule",command=self.setOnClickListener)
        self.botaoSee.grid(column=8,row=8,sticky="EW")

        self.crPassado = tkinter.Label(self, text="Seu C.R passado era:")
        self.crPassado.grid(column=0, row=8, sticky="EW")

        self.entryCrPassado = tkinter.Entry(self)
        self.entryCrPassado.grid(column=2, row=8, sticky="EW")

        self.crAtual = tkinter.Label(self, text="Seu C.R atual é:")
        self.crAtual.grid(column=4, row=8, sticky="EW")

        self.entryCrAtual = tkinter.Entry(self)
        self.entryCrAtual.grid(column=6, row=8, sticky="EW")

    def setOnClickListener(self):

        AdmSI1 = float(self.entryAdmSI1.get())
        AdmSI2 = float(self.entryAdmSI2.get())
        AdmSI3 = float(self.entryAdmSI3.get())
        AdmSIMed = (AdmSI1 + AdmSI2 + AdmSI3) / 3

        self.entryAdmSIMed.delete(0, tkinter.END)
        self.entryAdmSIMed.insert(0, str(AdmSIMed))

        AdmEst1 = str(self.entryAdmEst1.get())
        AdmEst2 = str(self.entryAdmEst2.get())
        AdmEst3 = str(self.entryAdmEst3.get())

        AdmEstMed = (float(AdmEst1) + float(AdmEst2) + float(AdmEst3)) / 3

        self.entryAdmEstMed.delete(0,tkinter.END)
        self.entryAdmEstMed.insert(0, str(AdmEstMed))

        Calc1 = float(self.entryCalc1.get())
        Calc2 = float(self.entryCalc2.get())
        Calc3 = float(self.entryCalc3.get())
        CalcMed = (Calc1 + Calc2 + Calc3) / 3

        self.entryCalcMed.delete(0, tkinter.END)
        self.entryCalcMed.insert(0, str(CalcMed))

        Web01 = float(self.entryWeb01.get())
        Web02 = float(self.entryWeb02.get())
        Web03 = float(self.entryWeb03.get())
        Web0Med = (Web01 + Web02 + Web03) / 3

        self.entryWeb0Med.delete(0, tkinter.END)
        self.entryWeb0Med.insert(0, str(Web0Med))

        LPII1 = float(self.entryLPII1.get())
        LPII2 = float(self.entryLPII2.get())
        LPII3 = float(self.entryLPII3.get())
        LPIIMed = (LPII1 + LPII2 + LPII3) / 3

        self.entryLPIIMed.delete(0, tkinter.END)
        self.entryLPIIMed.insert(0, str(LPIIMed))

        Psico1 = float(self.entryPsico1.get())
        Psico2 = float(self.entryPsico2.get())
        Psico3 = float(self.entryPsico3.get())
        PsicoMed = (Psico1 + Psico2 + Psico3) / 3

        self.entryPsicoMed.delete(0, tkinter.END)
        self.entryPsicoMed.insert(0, str(PsicoMed))

        CrPassado = str(self.entryCrPassado.get())
        MediaDisc = (AdmEstMed + AdmSIMed + CalcMed + LPIIMed + Web0Med + PsicoMed) / 6
        CrAtual = (float(CrPassado) + MediaDisc)/2

        self.entryCrAtual.delete(0,tkinter.END)
        self.entryCrAtual.insert(0,str(CrAtual))

if (__name__ == "__main__"):
    app = minhaApp_tk(None)  # criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Meu C.R baixo!')  # especificamos o título de nossa aplicação
    app.mainloop()