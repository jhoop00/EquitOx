# GUI
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import tkinter.font as font

spO2 = [i for i in range(101)]

#from serial import Serial
#serial_port = Serial('/dev/cu.usbmodem141301', 9600) # INSERT PORT NAME HERE

master = tk.Tk()

master.configure(bg='white')

# Set Logo Icon
img = (Image.open("E_Logo.png"))
resized_image= img.resize((50,50),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
master.iconphoto(False, new_image)

# Screen Dimensions
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
master.geometry(str(screen_width)+"x"+str(screen_height))

# Screen Logo 
canvas = tk.Canvas(master,width=int(screen_width*0.5),height=int(screen_height*0.5))
img = (Image.open("Logo.png"))
resized_image= img.resize((650,250),Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(screen_width*0.25,screen_height*0.25,image=new_image)
canvas.pack(expand=True)

def calibrateCommand():
    # serial_port.write(bytes('calibrate;','utf-8'));
    calibrateWindow = tk.Toplevel(master)
    calibrateWindow.title("Calibrate")
    calibrateLabel = tk.Label(calibrateWindow,text="INSERT CALIBRATION INSTRUCTIONS AND DIAGRAM")
    calibrateLabel.pack(expand=True)
    calibrate_button.pack_forget()
    return

def runCommand():
    # serial_port.write(bytes('run;','utf-8'));
    runWindow = tk.Toplevel(master)
    runWindow.title("Continuous Finger Monitoring")
    runLabel = tk.Label(runWindow,text="INSERT INSTRUCTIONS FOR CONTINUOUS FINGER MONITORING")
    runLabel.pack(expand=True)
    run_button.pack_forget()
    canvas.pack_forget()
    plotCommand()
    return

def plotCommand():
    fig = Figure(figsize = (5, 5),dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(spO2)
    canvas = FigureCanvasTkAgg(fig,master = master)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,master)
    canvas.get_tk_widget().pack()

def testHardware():
    return
    
test_button = tk.Button(master,text="Test Hardware Components",font=font.Font(size=20),command=calibrateCommand,padx=30,height=2,width=17)
test_button.pack()

blank_label = tk.Label(master,text=" ",pady=10)
blank_label.pack()


calibrate_button = tk.Button(master,text="Calibrate",font=font.Font(size=20),command=calibrateCommand,padx=30,height=2,width=17)
calibrate_button.pack()

blank_label = tk.Label(master,text=" ",pady=10)
blank_label.pack()

run_button = tk.Button(master,text="Continuous Finger Monitoring",font=font.Font(size=20),command=runCommand,padx=30,height=2,width=17)
run_button.pack()

blank_label = tk.Label(master,text=" ",pady=30)
blank_label.pack()

master.title("Equitox")

master.mainloop()

