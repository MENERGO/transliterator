from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox


def newfile(event=None):
    mw.title('Новая_Транслитерация')
    field.delete(1.0, END)
    result.delete(1.0, END)


def openfile(event=None):
    filename = filedialog.askopenfilename(filetypes=(('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')))
    try:
        with open(filename, 'r') as file:
            field.delete(1.0, END)
            field.insert(1.0, file.read())
            mw.title(filename.split('/')[-1])
    except:
        pass


def savefile(event=None):
    filename = filedialog.asksaveasfilename(filetypes=(('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')))
    if filename != '':
        with open(filename + '.txt', 'w') as file:
            file.write(result.get(1.0, END).rstrip('\n'))
            mw.title(filename.split('/')[-1])


def close(event=None):
    if messagebox.askyesno('Выход', 'Закрыть программу?'):
        mw.quit()


def helps():
    help_win = Toplevel()
    help_win.title('Справка')
    help_win.wm_iconbitmap('bsi.ico')
    help_win.geometry('400x420')
    help_win.resizable(False, False)
    text_help = """
    ТРАНСЛИТЕРАЦИЯ КИРИЛЛИЦЫ - СТАНДАРТ BSI
    Настоящий стандарт распространяется на правила
    транслитерации средствами латинского алфавита
    отдельных букв, слов, выражений, а также
    связанных текстов на языках, письменность
    которых базируется на кирилловском алфавите.
    Правила согласно настоящему стандарту применяют
    везде, где требуется обеспечить однозначное
    представление кирилловского текста латинскими
    буквами и возможность алгоритмического восстановления
    текста в исходной кирилловской записи, в частности
    при передаче документов по компьютерным сетям.
    Настоящий стандарт не распространяется на правила
    передачи латинскими буквами звукового облика слов,
    записанных кириллицей.

    а – a	к – k	х – kh	 
    б – b	л – l	ц – ts	 
    в – v	м – m	ч – ch	 
    г – g	н – n	ш – sh	 
    д – d	о – o	щ – shch	 
    е – e	п – p	ъ – ''	 
    ё – e	р – r	ы – y	 
    ж – zh	с – s	ь – '	 
    з – z	т – t	э – e	 
    и – i	у – u	ю – yu	 
    й – i	ф – f	я – ya	 
        """
    label_help = Label(help_win, text=text_help, justify=LEFT, width=60)
    label_help.pack()
    btn_close = Button(help_win, text='Ok', command=help_win.destroy)
    btn_close.place(x=320, y=380, width=65)


def about():
    about_win = Toplevel()
    about_win.title('О программе')
    about_win.geometry('400x420')
    about_win.resizable(False, False)
    text_about = """
            Транслитератор
        _______________________________________________________

        Version 1 (Build 1)
        © Nikita Litvinov, 2019
        Программа реализует транслитерацию
        из кириллицы по стандарту BSI.

        This product is PUBLIC DOMAIN
        and may be used AS IS, with all
        advantages and faults, in whole
        or in part, by anyone for any
        purpose, WITHOUT ANY CONDITIONS.

        _______________________________________________________

        transliterator@kartgeocentre.ru
            """
    label_about = Label(about_win, text=text_about, justify=LEFT, width=60)
    label_about.pack()
    btn_close = Button(about_win, text='Ok', command=about_win.destroy)
    btn_close.place(x=320, y=380, width=65)


def paste():
    field.event_generate("<<Paste>>")


def cut():
    field.event_generate("<<Cut>>")


def copy():
    field.event_generate("<<Copy>>")


def translit():
    result.delete(1.0, END)
    result.insert(1.0, latinisator(field.get(1.0, END), bsi))


def latinisator(letter, dict):
    for i, j in dict.items():
        letter = letter.replace(i, j).rstrip('\n')
    return letter


def clear():
    field.delete(1.0, END)
    result.delete(1.0, END)


def copyR():
    result.clipboard_clear()
    result.clipboard_append(result.get(1.0, END).rstrip('\n'))
    result.update()


def popup(event):
    popupmenu.tk_popup(event.x_root, event.y_root)


bsi = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': '"',
    'ы': 'y',
    'ь': "'",
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'Kh',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ъ': '"',
    'Ы': 'Y',
    'Ь': "'",
    'Э': 'E',
    'Ю': 'Yu',
    'Я': 'Ya',
}

mw = Tk()
mw.title('Транлитерация')
mw.wm_iconbitmap('bsi.ico')
mw.geometry('640x260')
mw.resizable(False, False)

mb = Menu()
mw.config(menu=mb)
filemenu = Menu(mb, tearoff=0)
filemenu.add_command(label='Новый', command=newfile, accelerator='Ctrl+N')
filemenu.add_command(label='Открыть', command=openfile, accelerator='Ctrl+O')
filemenu.add_command(label='Сохранить', command=savefile, accelerator='Ctrl+S')
filemenu.add_command(label='Выход', command=close, accelerator='Ctrl+Q')
helpmenu = Menu(mb, tearoff=0)
helpmenu.add_command(label='Справка', command=helps)
helpmenu.add_command(label='О программе', command=about)
mb.add_cascade(label='Файл', menu=filemenu)
mb.add_cascade(label='Помощь', menu=helpmenu)

panelL = Frame(mw)
panelR = Frame(mw)
TextFrame = Frame(mw)
txtFrame = Frame(mw)

field = scrolledtext.ScrolledText(TextFrame, width=33, height=10, font='Arial 12', wrap='word')
result = scrolledtext.ScrolledText(txtFrame, width=33, height=10, font='Arial 12', wrap='word')
field.focus()
field.pack()
result.pack()

label_title = Label(panelL, text='Транслитерация по стандарту bsi')
label_title.grid(column=0, row=0, columnspan=2)
label_l = Label(panelL, text='ИСХОДНЫЙ ТЕКСТ', font=("Open Sans", 8))
label_l.grid(column=0, row=1)
btn_paste = Button(panelL, text='Вставить', command=paste)
btn_paste.grid(column=1, row=1)
btn_latin = Button(panelL, text='Транслитерировать', command=translit)
btn_latin.grid(column=2, row=1)

label_empty = Label(panelR, text='')
label_empty.grid(column=0, row=0)
label_r = Label(panelR, text='ТРАНСЛИТЕРАЦИЯ', font=("Open Sans", 8))
label_r.grid(column=0, row=1)
btn_clear = Button(panelR, text='Очистить', command=clear)
btn_clear.grid(column=1, row=1)
btn_copy = Button(panelR, text='Скопировать', command=copyR)
btn_copy.grid(column=2, row=1)

panelL.grid(column=0, row=1)
panelR.grid(column=1, row=1)
TextFrame.grid(column=0, row=2)
txtFrame.grid(column=1, row=2)

popupmenu = Menu(field, tearoff=0)
popupmenu.add_command(label='Вырезать', command=cut)
popupmenu.add_command(label='Копировать', command=copy)
popupmenu.add_command(label='Вставить', command=paste)

field.bind("<Button-3>", popup)
field.bind("<Control-n>", newfile)
field.bind("<Control-o>", openfile)
field.bind("<Control-s>", savefile)
field.bind("<Control-q>", close)

mw.mainloop()
