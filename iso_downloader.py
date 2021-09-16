import tkinter as tk
from tkinter import Button, IntVar, StringVar, Variable, ttk
from tkinter.constants import BOTH, X
import webbrowser as wb
import os

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
officeDownLinks = {
    "Office 365": {
        "home_pre": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=f548523a",
            "French": "https://tb.rg-adguard.net/dl.php?go=19563d95",
            "English": "https://tb.rg-adguard.net/dl.php?go=ce412915",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=8d3bf668"
        },
        "Business": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=fff2f669",
            "French": "https://tb.rg-adguard.net/dl.php?go=c31af272",
            "English": "https://tb.rg-adguard.net/dl.php?go=beceea13",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=e55ccadf"
        },
        "pro_plus": {
            "Arabic": "https://tb.rg-adguard.net/dl.php?go=78674cf8",
            "French": "https://tb.rg-adguard.net/dl.php?go=f6561968",
            "English": "https://tb.rg-adguard.net/dl.php?go=287bd637",
            "Portuguese": "https://tb.rg-adguard.net/dl.php?go=9f6eaeec"
        }
    },
    "Office 2019": {
        "hom_stu": {
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/HomeStudent2019Retail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/HomeStudent2019Retail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/HomeStudent2019Retail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/HomeStudent2019Retail.img"
        },
        "hom_bus": {
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/HomeBusiness2019Retail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/HomeBusiness2019Retail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/HomeBusiness2019Retail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/HomeBusiness2019Retail.img"
        },
        "pro_plus": {
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/ProPlus2019Retail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/ProPlus2019Retail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/ProPlus2019Retail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/ProPlus2019Retail.img"
        }
    },
    "Office 2016": {
        "hom_stu":{
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/HomeStudentRetail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/HomeStudentRetail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/HomeStudentRetail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/HomeStudentRetail.img"
        },
        "hom_bus": {
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/HomeBusinessRetail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/HomeBusinessRetail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/HomeBusinessRetail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/HomeBusinessRetail.img"
        },
        "pro_plus": {
            "Arabic": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/ar-SA/ProPlusRetail.img",
            "French": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/fr-FR/ProPlusRetail.img",
            "English": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/en-US/ProPlusRetail.img",
            "Portuguese": "https://officecdn.microsoft.com/db/492350F6-3A01-4F97-B9C0-C7C6DDF67D60/media/pt-PT/ProPlusRetail.img"
        }
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
        self.aboutFrame = ttk.Frame(self.notebook)
        self.notebook.add(self.windowsFrame, text="Windows", )
        self.notebook.add(self.officeFrame, text="Office")
        self.notebook.add(self.aboutFrame, text="About")
        self.notebook.pack(expand=True, fill="both")
        self.osFrame.place(x=0, y=0)
        self.add_windows_in_nb()
        self.add_office_in_nb()
        self.about_section()

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
            self.officeLangMenu.set('')
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

    def add_office_in_nb(self):
        def office365ReDirect():
            self.officeRefer = 'Office 365'
            self.officeVer(self.officeRefer)

        def office2019ReDirect():
            self.officeRefer = 'Office 2019'
            self.officeVer(self.officeRefer)

        def office2016ReDirect():
            self.officeRefer = 'Office 2016'
            self.officeVer(self.officeRefer)

        style = ttk.Style()
        style.configure('W.TButton', font="calibri 15")
        ttk.Button(self.officeFrame, text="Office 365",
                   command=office365ReDirect, style='W.TButton').pack(pady=10)
        ttk.Button(self.officeFrame, text="Office 2019",
                   command=office2019ReDirect, style='W.TButton').pack(pady=10)
        ttk.Button(self.officeFrame, text="Office 2016",
                   command=office2016ReDirect, style='W.TButton').pack(pady=10)

    def officeVer(self, Refer):
        try:
            self.officeLangMenu.set('')
            self.winLangMenu.set('')
        except:
            pass
        self.officeVar = StringVar()
        ttk.Label(text="Select Edition : ",
              font="calibri 21").place(x=205, y=25)
        self.officeVerMenu = ttk.Combobox(
            self, textvariable=self.officeVar, width=40, font="calibri 14", justify="center")
        self.officeVerMenu['values'] = officeDict[Refer]['Edition']
        self.officeVerMenu['state'] = 'readonly'
        self.officeVerMenu.place(x=395, y=31)
        self.officeVerMenu.bind("<<ComboboxSelected>>", lambda refer=Refer: self.officeLang(Refer))

    def officeLang(self, Refer):
        self.officelangVar = StringVar()
        tk.Label(text="Select Language : ",
                 font="calibri 21").place(x=205, y=80)
        self.officeLangMenu = ttk.Combobox(
            self, textvariable=self.officelangVar, width=37, font="calibri 14", justify="center")
        self.officeLangMenu['values'] = officeDict[Refer]['lang']
        self.officeLangMenu['state'] = 'readonly'
        self.officeLangMenu.place(x=425, y=87)
        self.officeLangMenu.bind("<<ComboboxSelected>>", lambda refer=Refer: self.officeDownButton(Refer))

    def officeDownButton(self, Refer):
        self.style = ttk.Style()
        self.style.configure("Kim.TButton", font="calibri 17")
        ttk.Button(self, text='Download', style='Kim.TButton', command=lambda refer=Refer: self.officeDownload(Refer)).place(x=205, y=130)

    def officeDownload(self, Refer):
        self.officever = self.officeVar.get()
        self.officelang = self.officelangVar.get()
        if Refer=="Office 365":
            if self.officever=="Home Premium":
                self.officeverid = "home_pre"
            elif self.officever=="Business":
                self.officeverid = "Business"
            elif self.officever=="Professional Plus":
                self.officeverid = "pro_plus"
        elif Refer=="Office 2019" or Refer=="Office 2016":
            if self.officever=="Home Student":
                self.officeverid = "hom_stu"
            elif self.officever=="Home Business":
                self.officeverid = "hom_bus"
            elif self.officever=="Professional Plus":
                self.officeverid = "pro_plus"

        self.link = officeDownLinks[Refer][self.officeverid][self.officelang]
        wb.open(self.link)

    def about_section(self):
        self.path = '@%s' % os.path.join(os.environ['WINDIR'], 'Cursors/aero_link.cur').replace('\\', '/')
        self.label = tk.Label(self.aboutFrame, text='''
        ISO Downloader
        made by Abhinav

        v1.01
        ''',font="Calibri 10")
        self.label.place(x=0, y=0)
        self.hyperlink = tk.Label(self.aboutFrame, text="Github Website", font="Calibri 10 underline")
        self.hyperlink.configure(cursor=self.path)
        self.hyperlink.place(x=25, y=90)
        self.hyperlink.bind("<Button-1>", lambda self: wb.open("https://github.com/abhinav-dot/ISO-Downloader"))
        





if __name__ == "__main__":
    iso_downloader = Iso_Downloader()
    iso_downloader.create_frames_and_notebook()
    iso_downloader.mainloop()
