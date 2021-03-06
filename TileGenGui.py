import tkinter
import tkinter.filedialog as fdtk
import tkinter.ttk as ttk

import MapGenerator

class App(tkinter.Frame):

    def __init__(self, root, *args, **kwargs):
        tkinter.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.progressBarValue = tkinter.IntVar()
        self.imagePath = tkinter.StringVar()
        self.TileSizeEntry=tkinter.IntVar()
        self.zoomFactorEntry = tkinter.IntVar()
        self.interface()


    def interface(self):
        # Logo 
        logo_img = tkinter.PhotoImage(file ='logo.png')
        logo = tkinter.Label(image=logo_img)
        logo.image = logo_img
        logo.grid(row=0, column=0, columnspan=2)

        # File Explorer
        fileExplorer = tkinter.Button(text="Charger un fichier", command=self.openImage).grid(row=1, column=0)
        fileExplorerInfo = tkinter.Entry(textvariable=self.imagePath)
        fileExplorerInfo.grid(row=1, column=1)

        # Tile Size
        tileSize_label = tkinter.Label(text="Tile Size :")
        tileSize_label.grid(row=2, column=0)
        tileSize_input = tkinter.Entry(textvariable=self.TileSizeEntry)
        self.TileSizeEntry.set(256)
        tileSize_input.grid(row=2, column=1)
        
        # ZoomFactor
        zoomFactor_label = tkinter.Label(text="Zoom Factor :")
        zoomFactor_label.grid(row=3, column=0)
        zoomFactor_input = tkinter.Entry(textvariable=self.zoomFactorEntry)
        self.zoomFactorEntry.set(2)
        zoomFactor_input.grid(row=3, column=1)

        # ProgressBar
        self.progressBar = ttk.Progressbar(root, length=200)
        self.progressBar.grid(row=4, column=0, columnspan=2)

        # Generate
        generation_button = tkinter.Button(text="Generate", command=self.genTiles)
        generation_button.grid(row=5, column=0, columnspan=2)


    def incrementProgressBar(self):
        self.progressBarValue.set(self.progressBarValue.get() + 1)


    def genTiles(self):
        mapTile = MapGenerator.Map(
            self.imagePath.get(),
            tileSize = self.TileSizeEntry.get(),
            sizeFactor = self.zoomFactorEntry.get())
        
        self.progressBar.config(
            mode='determinate', 
            maximum=mapTile.numberTilesTotal, 
            variable=self.progressBarValue
            )
        generator = MapGenerator.MapGenerator(mapTile)

        for progress in generator.generateMapTiles():
            self.progressBarValue.set(progress)
            self.progressBar.update()

        
    def openImage(self):
        labelPath = fdtk.askopenfilename(
                initialdir = "E:/Images",
                title = "choose your file",
                filetypes = (
                                ("jpeg files","*.jpg"),
                                ("png files", "*.png"),
                                ("all files","*.*")
                            )
                )
        self.imagePath.set(labelPath)

root = tkinter.Tk()
app = App(root)
tkinter.mainloop()
