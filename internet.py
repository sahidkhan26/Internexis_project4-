from tkinter import *
import speedtest

root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")


def Check():
    test = speedtest.Speedtest()

    download_speed = test.download() / 1_000_000  # Convert to Mbps
    upload_speed = test.upload() / 1_000_000  # Convert to Mbps
    test.get_best_server()
    ping_result = test.results.ping

    # Update the labels with results
    ping.config(text=f"{ping_result:.2f}")
    download.config(text=f"{download_speed:.2f}")
    upload.config(text=f"{upload_speed:.2f}")
    Download.config(text=f"{download_speed:.2f}")


# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Images
Top = PhotoImage(file="top.png")
Label(root, image=Top, bg="#1a212d").pack()

Main = PhotoImage(file="main.png")
Label(root, image=Main, bg="#1a212d").pack(pady=(40, 0))

button_img = PhotoImage(file="button.png")
Button(root, image=button_img, bg="#1a212d", bd=0, activebackground="#1a212d",
       cursor="hand2", command=Check).pack(pady=10)

# Labels
Label(root, text="PING", font="arial 10 bold", bg="#384056").place(x=50, y=0)
Label(root, text="DOWNLOAD", font="arial 10 bold", bg="#384056").place(x=140, y=0)
Label(root, text="UPLOAD", font="arial 10 bold", bg="#384056").place(x=260, y=0)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=60, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=160, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=275, y=80)

Label(root, text="Download", font="arial 15 bold", bg="#384056", fg="white").place(x=140, y=280)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056", fg="white").place(x=155, y=380)

ping = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=70, y=60, anchor="center")

download = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=180, y=60, anchor="center")

upload = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=290, y=60, anchor="center")

Download = Label(root, text="00", font="arial 40 bold", bg="#384056", fg="white")
Download.place(x=185, y=350, anchor="center")

root.mainloop()
