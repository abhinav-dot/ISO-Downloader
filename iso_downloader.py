import tkinter as tk
from tkinter import Button, IntVar, StringVar, Variable, ttk
from tkinter.constants import BOTH, X
import webbrowser as wb

windowsOsDict = {
    "Windows 10": {
        "version": ("Windows 10 21H1 64 bit", "Windows 10 20H2 64 bit", "Windows 10 20H1 64 bit",
                    "Windows 10 21H1 32 bit", "Windows 10 20H2 32 bit", "Windows 10 20H1 32 bit"),
        "lang": ("Arabic", "French", "English International", "Portuguese", "Spanish")
    },
    "Windows 8.1": {
        "version": ("Windows 8.1 build 9600 64 bit", "Windows 8.1 build 9600 32 bit"),
        "lang": ("Arabic", "French", "English International", "Spanish")
    },
    "Windows 7": {
        "edition": ("Windows 7 Home Premium 64 bit", "Windows 7 Professional 64 bit", "Windows 7 Ultimate 64 bit", "Windows 7 Home Premium 32 bit", "Windows 7 Professional 32 bit", "Windows 7 Ultimate 32 bit"),
        "lang": ("English International", )
    },
}
winDownLinks = {
    "Windows 10": {
        "21H1_64": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=98a16b97",
            "French": "https://tb.rg-adguard.net/dl.php?go=e358396d",
            "English International": "https://tb.rg-adguard.net/dl.php?go=8c764d2e",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=b6ba9869",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=1e7c5fc4"
        },
        "20H2_64": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=5d1ad74c",
            "French": "https://tb.rg-adguard.net/dl.php?go=7e6ea65a",
            "English International": "https://tb.rg-adguard.net/dl.php?go=3dd1ce66",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=ce68b551",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=c19af683"
        },
        "20H1_64": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=65f35665",
            "French": "https://tb.rg-adguard.net/dl.php?go=f5637477",
            "English International": "https://tb.rg-adguard.net/dl.php?go=272d35a7",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=75accbf1",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=991543ac"
        },
        "21H1_32": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=ef3d13a3",
            "French": "https://tb.rg-adguard.net/dl.php?go=c1f389d1",
            "English International": "https://tb.rg-adguard.net/dl.php?go=d61c63b5",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=e18a9c18",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=4b7579db"
        },
        "20H2_32": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=bd76cfcf",
            "French": "https://tb.rg-adguard.net/dl.php?go=aa48d63c",
            "English International": "https://tb.rg-adguard.net/dl.php?go=7e583fea",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=fa227a94",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=bd9a2567"
        },
        "20H1_32": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=228dc62b",
            "French": "https://tb.rg-adguard.net/dl.php?go=c5e5c337",
            "English International": "https://tb.rg-adguard.net/dl.php?go=a621ee85",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=b8e587ed",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=5ede7de7"
        }
    },
    "Windows 8.1": {
        "9600_64": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=67f64b42",
            "French": "https://tb.rg-adguard.net/dl.php?go=8d7bdce9",
            "English International": "https://tb.rg-adguard.net/dl.php?go=1e2ec728",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=39d1db1f"
        },
        "9600_32": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=b6996789",
            "French": "https://tb.rg-adguard.net/dl.php?go=c5664f1d",
            "English International": "https://tb.rg-adguard.net/dl.php?go=948e15fe",
            "Spanish": "https://tb.rg-adguard.net/dl.php?go=d6839c41"
        }
    },
    "Windows 7": {
        "hp_64": "https://download.microsoft.com/download/E/A/8/EA804D86-C3DF-4719-9966-6A66C9306598/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_HOMEPREMIUM_x64FRE_en-us.iso",
        "pro_64": "https://download.microsoft.com/download/0/6/3/06365375-C346-4D65-87C7-EE41F55F736B/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_PROFESSIONAL_x64FRE_en-us.iso",
        "ult_64": "https://download.microsoft.com/download/5/1/9/5195A765-3A41-4A72-87D8-200D897CBE21/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_ULTIMATE_x64FRE_en-us.iso",
        "hp_32": "https://download.microsoft.com/download/E/D/A/EDA6B508-7663-4E30-86F9-949932F443D0/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_HOMEPREMIUM_x86FRE_en-us.iso",
        "pro_32": "https://download.microsoft.com/download/C/0/6/C067D0CD-3785-4727-898E-60DC3120BB14/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_PROFESSIONAL_x86FRE_en-us.iso",
        "ult_32": "https://download.microsoft.com/download/1/E/6/1E6B4803-DD2A-49DF-8468-69C0E6E36218/7601.24214.180801-1700.win7sp1_ldr_escrow_CLIENT_ULTIMATE_x86FRE_en-us.iso"
    }
}
officeDict = {
    "Office 365": {
        "Edition": ("Home Premium", "Business", "Professional Plus"),
        "lang": ("Arabic", "French", "English", "Portuguese")
    },
    "Office 2019": {
        "Edition": ("Home Student", "Home Business", "Professional Plus"),
        "lang": ("Arabic", "French", "English", "Portuguese")
    },
    "Office 2016": {
        "Edition": ("Home Student", "Home Business", "Professional Plus"),
        "lang": ("Arabic", "French", "English", "Portuguese")
    }
}


class Iso_Downloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x500")
        self.resizable(width=False, height=False)
        self.title("ISO Downloader 1.01")
        self.var = StringVar()
        self.wm_iconbitmap("iso.ico")

    def create_frames_and_notebook(self):
        self.osFrame = ttk.Frame()
        self.osFrame['padding'] = (0, 0, 50, 500)
        self.osFrame['borderwidth'] = 5
        self.osFrame['relief'] = 'sunken'
        self.notebook = ttk.Notebook(self.osFrame)
        self.windowsFrame = ttk.Frame(self.notebook)
        self.officeFrame = ttk.Frame(self.notebook)
        self.notebook.add(self.windowsFrame, text="windows", )
        self.notebook.add(self.officeFrame, text="office")
        self.notebook.pack(expand=True, fill="both")
        self.osFrame.place(x=0, y=0)
        self.add_windows_in_nb()

    def add_windows_in_nb(self):
        def win10ReDirect():
            self.winRefer = 'Windows 10'
            self.winVer(self.winRefer)

        def win8ReDirect():
            self.winRefer = 'Windows 8.1'
            self.winVer(self.winRefer)

        def win7ReDirect():
            self.winRefer = 'Windows 7'
            self.winVer(self.winRefer, type='edition')
        style = ttk.Style()
        style.configure('W.TButton', font="calibri 15")
        ttk.Button(self.windowsFrame, text="Windows 10",
                   command=win10ReDirect, style='W.TButton').pack(pady=10)
        ttk.Button(self.windowsFrame, text="Windows 8.1",
                   command=win8ReDirect, style='W.TButton').pack(pady=10)
        ttk.Button(self.windowsFrame, text="Windows 7",
                   command=win7ReDirect, style='W.TButton').pack(pady=10)

    def winVer(self, Refer, type='version'):
        try:
            self.winLangMenu.set('')
        except:
            pass
        self.var = StringVar()
        ttk.Label(text="Select Edition : ",
                  font="calibri 21").place(x=205, y=25)
        self.winVerMenu = ttk.Combobox(
            self, textvariable=self.var, width=40, font="calibri 14", justify="center")
        self.winVerMenu['values'] = windowsOsDict[Refer][type]
        self.winVerMenu['state'] = 'readonly'
        self.winVerMenu.place(x=395, y=31)
        self.winVerMenu.bind("<<ComboboxSelected>>",
                             lambda refer=Refer: self.winLang(Refer))

    def winLang(self, Refer):
        self.langVar = StringVar()
        tk.Label(text="Select Language : ",
                 font="calibri 21").place(x=205, y=80)
        self.winLangMenu = ttk.Combobox(
            self, textvariable=self.langVar, width=37, font="calibri 14", justify="center")
        self.winLangMenu['values'] = windowsOsDict[Refer]['lang']
        self.winLangMenu['state'] = 'readonly'
        self.winLangMenu.place(x=425, y=87)
        self.winLangMenu.bind("<<ComboboxSelected>>",
                              lambda refer=Refer: self.winDownloadButton(Refer))

    def winDownloadButton(self, Refer):
        self.style = ttk.Style()
        self.style.configure("Kim.TButton", font="calibri 17")
        ttk.Button(self, text='Download', style='Kim.TButton',
                   command=lambda refer=Refer: self.winDownload(refer)).place(x=205, y=130)

    def winDownload(self, Refer):
        self.winver = self.var.get()
        self.langvar = self.langVar.get()
        if Refer == "Windows 10":
            if self.winver == "Windows 10 21H1 64 bit":
                self.winverid = "21H1_64"
            elif self.winver == "Windows 10 20H2 64 bit":
                self.winverid = "20H2_64"
            elif self.winver == "Windows 10 20H1 64 bit":
                self.winverid = "20H1_64"
            elif self.winver == "Windows 10 21H1 32 bit":
                self.winverid = "21H1_32"
            elif self.winver == "Windows 10 20H2 32 bit":
                self.winverid = "20H2_32"
            elif self.winver == "Windows 10 20H1 32 bit":
                self.winverid = "20H1_32"
        elif Refer == "Windows 8.1":
            if self.winver == "Windows 8.1 build 9600 64 bit":
                self.winverid = "9600_64"
            elif self.winver == "Windows 8.1 build 9600 32 bit":
                self.winverid = "9600_32"
        elif Refer == "Windows 7":
            if self.winver == "Windows 7 Home Premium 64 bit":
                self.winverid = "hp_64"
            elif self.winver == "Windows 7 Professional 64 bit":
                self.winverid = "pro_64"
            elif self.winver == "Windows 7 Ultimate 64 bit":
                self.winverid = "ult_64"
            elif self.winver == "Windows 7 Home Premium 32 bit":
                self.winverid = "hp_32"
            elif self.winver == "Windows 7 Professional 32 bit":
                self.winverid = "pro_32"
            elif self.winver == "Windows 7 Ultimate 32 bit":
                self.winverid = "ult_32"
        if Refer == "Windows 10" or Refer == "Windows 8.1":
            self.link = winDownLinks[Refer][self.winverid][self.langvar]
        else:
            self.link = winDownLinks[Refer][self.winverid]
        wb.open(self.link)


if __name__ == "__main__":
    iso_downloader = Iso_Downloader()
    iso_downloader.create_frames_and_notebook()
    iso_downloader.mainloop()
