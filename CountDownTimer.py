import tkinter as t

window = t.Tk()
input_frame = t.Frame(window)
countdown_frame = t.Frame(window)
window.title("CountDown Timer")
window.geometry("400x150")


class CountDownTimer:
    def __init__(self, frame, number, container):
        self.frame = frame
        self.number = number
        self.paused = False
        self.container = container

        self.frame.pack(fill="both", expand=1)

        minutes, seconds = divmod(self.number, 60)
        self.counting_label = t.Label(self.frame, text="{:02d}:{:02d}".format(minutes, seconds))
        self.counting_label.pack()

        self.start_button = t.Button(self.frame, text="Start", command=self.update_the_time)
        self.start_button.pack()

        self.pause_button = t.Button(self.frame, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.resume_button = t.Button(self.frame, text="Resume", command=self.resume)
        self.resume_button.pack()

        self.stop_button = t.Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.pack()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.container.destroy()

    def update_the_time(self):
        self.start_button.destroy()
        if not self.paused and self.number != 0:
            self.number -= 1
            minutes, seconds = divmod(self.number, 60)
            self.counting_label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
        self.container.after(1000, self.update_the_time)

        if self.number == 0:
            self.counting_label.configure(text="Timer Over!")


def getting_input():
    input_frame.pack(fill='both', expand=1)

    inp_label = t.Label(input_frame, text="Enter the seconds to countdown: ")
    inp_label.pack()
    inp_entry = t.Entry(input_frame)
    inp_entry.pack()
    submit_button = t.Button(input_frame, text="Enter", command=lambda: get_input(inp_entry))
    submit_button.pack()


def get_input(widget):
    input_value = widget.get()
    destroy_widgets_of(input_frame)

    try:
        input_value = int(input_value)
    except ValueError:
        t.Label(input_frame, text="Enter Positive Integer Values!").pack()
        getting_input()

    if isinstance(input_value, int):
        input_frame.pack_forget()
        timer_object = CountDownTimer(countdown_frame, input_value, window)


def destroy_widgets_of(frame):
    for widget in frame.winfo_children():
        widget.destroy()


getting_input()

window.mainloop()
