from tkinter import *
from PIL import Image, ImageTk

root1 = Tk()
root1.title('Leather Tree London')
root1.geometry('1500x1000')
basket_content = StringVar()

def show_shop_him():
    lower_frame.grid_forget()
    basket_frame.grid_forget()
    shop_frame_him.grid(row=0, column=0)

def show_shop_her():
    lower_frame.grid_forget()
    basket_frame.grid_forget()
    shop_frame_her.grid(row=0, column=0)

def show_shop_sale():
    lower_frame.grid_forget()
    basket_frame.grid_forget()
    shop_frame_sale.grid(row=0, column=0)


items = []
prices = []
def show_basket():
    shop_frame_him.grid_forget()
    shop_frame_her.grid_forget()
    shop_frame_sale.grid_forget()
    basket_frame.grid(row=0, column=0)
    c = 1
    for item, price in zip(items, prices):
        Label(item_frame, text=f'{c}.\t Name: {item}  Price: {price} \n').pack()
        c += 1


def add(item, price, counter=None):
    items.append(item)
    prices.append(price)
    counter.set(counter.get() + 1)
    print(items)



# ----------------Top_Frame----------------------
top_frame = LabelFrame(width=400, height=200, bg='White')
top_frame.pack(padx=15, pady=5)

#GRIDS_lines_ Right
right_line = LabelFrame(master=top_frame, width=3, height=350, bg='black')
right_line.grid(row=0, column=0, padx=5, pady=5)
right1_line = LabelFrame(master=top_frame, width=3, height=350, bg='black')
right1_line.grid(row=0, column=1, padx=5, pady=5)
right2_line = LabelFrame(master=top_frame, width=3, height=350, bg='black')
right2_line.grid(row=0, column=2, padx=5, pady=5)

#LOGO_Grids
logo_button = LabelFrame(master=top_frame, width=210, height=250, bg='white')
logo_button.grid(row=0, column=3, padx=(0,10), pady=0)

#LABEL_Grids
label_frame = LabelFrame(master=top_frame, width=100, height=50, bg='white')
label_frame.grid(row=0, column=4, padx=(0,200), pady=0)
label = Label(label_frame, text="WELCOME TO LEATHER TREE ZARSHAM", bg='White', font=('Chalkduster', 30, 'bold'))
label.grid(row=1, column=2, padx=(0, 200), pady=1)

#Grids_Line_Top
top_line = LabelFrame(master=label_frame, width=500, height=3, bg='black')
top_line.grid(row=0, column=2,padx=5, pady=5)

#Grids_Lines_Buttom
line_frame1B = LabelFrame(master=label_frame, width=800, height=3, bg='black')
line_frame1B.grid(row=2, column=2, padx=0, pady=5)
line_frame2B = LabelFrame(master=label_frame, width=800, height=3, bg='black')
line_frame2B.grid(row=3, column=2, padx=0, pady=5)
line_frame3B = LabelFrame(master=label_frame, width=800, height=3, bg='black')
line_frame3B.grid(row=4, column=2, padx=0, pady=5)
line_frame4B = LabelFrame(master=label_frame, width=800, height=3, bg='black')
line_frame4B.grid(row=5, column=2, padx=0, pady=5)

#Bottom_Grid_Search
bottom_frame = LabelFrame(master=label_frame, width=800, height=50, bg='white')
bottom_frame.grid(row=6, column=2 ,padx=(50,0), pady=5)

#Grids_Line_Left
left_line = LabelFrame(master=top_frame, width=3, height=250, bg='black')
left_line.grid(row=0, column=5, padx=5, pady=(0,5))
left_line1 = LabelFrame(master=top_frame, width=3, height=250, bg='black')
left_line1.grid(row=0, column=6, padx=5, pady=(0,5))
left_line2 = LabelFrame(master=top_frame, width=3, height=250, bg='black')
left_line2.grid(row=0, column=7, padx=5, pady=(0,5))

#LOGO_Image
image = Image.open('LT_Screenshot.jpg')
resized_image = image.resize((210, 250))
photo = ImageTk.PhotoImage(resized_image)
logo_button = Label(logo_button, image=photo)
logo_button.image = photo
logo_button.grid(row=0, column=0, padx=5, pady=5)
right_line.grid(row=0, column=0, padx=5, pady=5)


#Search, Basket_Frame_Grids
counter = IntVar(value=0)

search_line = LabelFrame(master=bottom_frame, width=50, height=50, bg='White')
search_line.grid(row=0, column=1, padx=15, pady=5)
label = Button(search_line, text="SEARCH", bg='White', font=('Chalkduster', 15, 'bold'), width=10, height=2, bd=20, relief=FLAT, command=show_basket)
label.grid(row=0, column=3, padx=15, pady=5)

basket_line = LabelFrame(master=bottom_frame, width=50, height=50, bg='White')
basket_line.grid(row=0, column=3, padx=15, pady=5)
label = Button(basket_line, text="BASKET", bg='White', font=('Chalkduster', 15, 'bold'), width=10, height=2, bd=20, relief=FLAT, command=show_basket)
label.grid(row=0, column=1, padx=15, pady=5)

counter_basket_button = Button(master=bottom_frame, textvariable=counter, font=('chalkduster',14,'bold'))
counter_basket_button.grid(row=0, column=2,padx=25, pady=5)


# --------------- Lower_Frame ---------------------------------
lower_frame = LabelFrame(width=1000, height=1000, bg='white')
lower_frame.pack(padx=5, pady=20)


#HIM_BUTTON
frame_button = LabelFrame(master=lower_frame, width=300, height=300, bg='WHITE')
frame_button.grid(row=0, column=0, padx=140, pady=(50,10))

image = Image.open('VK.jpg')
resized_image = image.resize((250, 300))
photo = ImageTk.PhotoImage(resized_image)
photo_label = Label(frame_button, image=photo)
photo_label.image = photo
photo_label.grid(row=1, column=0)

lb_text = Button(frame_button, text='HIM', font=('Chalkduster',25), width=10, height=2, bd=20, relief=FLAT, command=show_shop_him)
lb_text.grid(padx=5, pady=0, row=0, column=0)


#HER_BUTTON
frame_button1 = LabelFrame(master=lower_frame, width=300, height=300, bg='WHITE')
frame_button1.grid(row=0, column=1, padx=120, pady=(50,10))

image = Image.open('KS.jpg')
resized_image = image.resize((250, 300))
photo = ImageTk.PhotoImage(resized_image)
photo_label = Label(frame_button1, image=photo)
photo_label.image = photo
photo_label.grid(row=1, column=1)

lb_text = Button(frame_button1, text='HER', font=('Chalkduster',25), width=10, height=2, bd=20, relief=FLAT, command=show_shop_her)
lb_text.grid(padx=5, pady=0, row=0, column=1)


#SALE_BUTTON
frame_button2 = LabelFrame(master=lower_frame, width=300, height=300, bg='WHITE')
frame_button2.grid(row=0, column=2, padx=120, pady=(50,10))

image = Image.open('SLT.jpg')
resized_image = image.resize((250, 300))
photo = ImageTk.PhotoImage(resized_image)
photo_label = Label(frame_button2, image=photo)
photo_label.image = photo
photo_label.grid(row=1, column=2)

lb_text = Button(frame_button2, text='SALE', font=('Chalkduster',25), width=10, height=2, bd=20, relief=FLAT, command=show_shop_sale)
lb_text.grid(padx=5, pady=0, row=0, column=2)


# -------------------Last_Line3-------------------
line_frame1C = LabelFrame(master=root1, width=900, height=3, bg='black')
line_frame1C.pack(anchor= W, padx=5, pady=5)
line_frame2C = LabelFrame(master=root1, width=900, height=3, bg='black')
line_frame2C.pack(anchor= W, padx=5, pady=5)
line_frame3C = LabelFrame(master=root1, width=900, height=3, bg='black')
line_frame3C.pack(anchor= W, padx=5, pady=5)

#SHOP_FRAME_For_Him_Her_Sale

shop_frame_him = LabelFrame(lower_frame,width=1000, height=1000, background='black', relief=RAISED)
shop_frame_her = LabelFrame(lower_frame,width=1000, height=1000, background='black', relief=RAISED)
shop_frame_sale = LabelFrame(lower_frame,width=1000, height=1000, background='black', relief=RAISED)
basket_frame = LabelFrame(lower_frame, width=1000, height=1000, background='black', relief=RAISED)

#HIM1_to_HIM4_PRODUCT_Grid
Him1_frame = LabelFrame(shop_frame_him, width=100, height=150, background='white')
Him1_frame.grid(row=0, column=0,padx=5, pady=5)

Him2_frame = LabelFrame(shop_frame_him, width=100, height=150, background='white')
Him2_frame.grid(row=0, column=1,padx=5, pady=5)

Him3_frame = LabelFrame(shop_frame_him, width=100, height=150, background='white')
Him3_frame.grid(row=0, column=2,padx=5, pady=5)

Him4_frame = LabelFrame(shop_frame_him, width=100, height=150, background='white')
Him4_frame.grid(row=0, column=3,padx=5, pady=5)

#Him_Product_Image_From_Him1_to_Him4
Him1_label = Label(Him1_frame,font=('Chalkduster',25), text='HIM1')
image = Image.open('HIM1.jpg')
resized_image = image.resize((255, 300))
Him1_photo = ImageTk.PhotoImage(resized_image)
Him1_image_label = Label(Him1_frame, image=Him1_photo, bg='white')
Him1_price_label = Label(Him1_frame, font=('Chalkduster',25), text='£20', bg='white')
Him1_add_button = Button(Him1_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('HIM1', '£20', counter))
Him1_label.grid(row=0, column=0, padx=50,pady=30)
Him1_image_label.grid(row=1, column=0, padx=45, pady=5)
Him1_price_label.grid(row=2, column=0)
Him1_add_button.grid(row=3, column=0)


Him2_label = Label(Him2_frame,font=('Chalkduster',25), text='HIM2')
image = Image.open('HIM2.jpg')
resized_image = image.resize((255, 300))
Him2_photo = ImageTk.PhotoImage(resized_image)
Him2_image_label = Label(Him2_frame, image=Him2_photo, bg='white')
Him2_price_label = Label(Him2_frame, font=('Chalkduster',25), text='£20', bg='white')
Him2_add_button = Button(Him2_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('HIM2', '£20', counter))
Him2_label.grid(row=0, column=1, padx=50,pady=30)
Him2_image_label.grid(row=1, column=1, padx=45, pady=5)
Him2_price_label.grid(row=2, column=1)
Him2_add_button.grid(row=3, column=1)


Him3_label = Label(Him3_frame,font=('Chalkduster',25), text='HIM3')
image = Image.open('HIM3.jpg')
resized_image = image.resize((260, 300))
Him3_photo = ImageTk.PhotoImage(resized_image)
Him3_image_label = Label(Him3_frame, image=Him3_photo, bg='white')
Him3_price_label = Label(Him3_frame, font=('Chalkduster',25), text='£20', bg='white')
Him3_add_button = Button(Him3_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('HIM3', '£20', counter))
Him3_label.grid(row=0, column=0, padx=50,pady=30)
Him3_image_label.grid(row=1, column=0, padx=45, pady=5)
Him3_price_label.grid(row=2, column=0)
Him3_add_button.grid(row=3, column=0)


Him4_label = Label(Him4_frame,font=('Chalkduster',25), text='HIM4')
image = Image.open('HIM4.jpeg')
resized_image = image.resize((260, 300))
Him4_photo = ImageTk.PhotoImage(resized_image)
Him4_image_label = Label(Him4_frame, image=Him4_photo, bg='white')
Him4_price_label = Label(Him4_frame, font=('Chalkduster',25), text='£20', bg='white')
Him4_add_button = Button(Him4_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('HIM4', '£20', counter))
Him4_label.grid(row=0, column=1, padx=50,pady=30)
Him4_image_label.grid(row=1, column=1, padx=45, pady=5)
Him4_price_label.grid(row=2, column=1)
Him4_add_button.grid(row=3, column=1)


#HER1_to_HER4_PRODUCT_Grid
Her1_frame = LabelFrame(shop_frame_her, width=100, height=150, background='white')
Her1_frame.grid(row=0, column=0,padx=5, pady=5)

Her2_frame = LabelFrame(shop_frame_her, width=100, height=150, background='white')
Her2_frame.grid(row=0, column=1,padx=5, pady=5)

Her3_frame = LabelFrame(shop_frame_her, width=100, height=150, background='white')
Her3_frame.grid(row=0, column=2,padx=5, pady=5)

Her4_frame = LabelFrame(shop_frame_her, width=100, height=150, background='white')
Her4_frame.grid(row=0, column=3,padx=5, pady=5)


#Her_Product_Image_From_Her1_to_Her4
Her1_label = Label(Her1_frame,font=('Chalkduster',25), text='HER1')
image = Image.open('HER1.jpg')
resized_image = image.resize((255, 300))
Her1_photo = ImageTk.PhotoImage(resized_image)
Her1_image_label = Label(Her1_frame, image=Her1_photo, bg='white')
Her1_price_label = Label(Her1_frame, font=('Chalkduster',25), text='£20', bg='white')
Her1_add_button = Button(Her1_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('HER1', '£20', counter))
Her1_label.grid(row=0, column=0, padx=50,pady=30)
Her1_image_label.grid(row=1, column=0, padx=45, pady=5)
Her1_price_label.grid(row=2, column=0)
Her1_add_button.grid(row=3, column=0)


Her2_label = Label(Her2_frame,font=('Chalkduster',25), text='HER2')
image = Image.open('HER2.jpg')
resized_image = image.resize((255, 300))
Her2_photo = ImageTk.PhotoImage(resized_image)
Her2_image_label = Label(Her2_frame, image=Her2_photo, bg='white')
Her2_price_label = Label(Her2_frame, font=('Chalkduster',25), text='£20', bg='white')
Her2_add_button = Button(Her2_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('HER2', '£20', counter))
Her2_label.grid(row=0, column=1, padx=50,pady=30)
Her2_image_label.grid(row=1, column=1, padx=45, pady=5)
Her2_price_label.grid(row=2, column=1)
Her2_add_button.grid(row=3, column=1)


Her3_label = Label(Her3_frame,font=('Chalkduster',25), text='HER3')
image = Image.open('HER3.jpg')
resized_image = image.resize((260, 300))
Her3_photo = ImageTk.PhotoImage(resized_image)
Her3_image_label = Label(Her3_frame, image=Her3_photo, bg='white')
Her3_price_label = Label(Her3_frame, font=('Chalkduster',25), text='£20', bg='white')
Her3_add_button = Button(Her3_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('HER3', '£20', counter))
Her3_label.grid(row=0, column=0, padx=50,pady=30)
Her3_image_label.grid(row=1, column=0, padx=45, pady=5)
Her3_price_label.grid(row=2, column=0)
Her3_add_button.grid(row=3, column=0)


Her4_label = Label(Her4_frame,font=('Chalkduster',25), text='HER4')
image = Image.open('HER4.jpg')
resized_image = image.resize((260, 300))
Her4_photo = ImageTk.PhotoImage(resized_image)
Her4_image_label = Label(Her4_frame, image=Her4_photo, bg='white')
Her4_price_label = Label(Her4_frame, font=('Chalkduster',25), text='£20', bg='white')
Her4_add_button = Button(Her4_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('HER4', '£20', counter))
Her4_label.grid(row=0, column=1, padx=50,pady=30)
Her4_image_label.grid(row=1, column=1, padx=45, pady=5)
Her4_price_label.grid(row=2, column=1)
Her4_add_button.grid(row=3, column=1)


#SALE1_to_SALE4_PRODUCT_Grid
Sale1_frame = LabelFrame(shop_frame_sale, width=100, height=150, background='white')
Sale1_frame.grid(row=0, column=0,padx=5, pady=5)

Sale2_frame = LabelFrame(shop_frame_sale, width=100, height=150, background='white')
Sale2_frame.grid(row=0, column=1,padx=5, pady=5)

Sale3_frame = LabelFrame(shop_frame_sale, width=100, height=150, background='white')
Sale3_frame.grid(row=0, column=2,padx=5, pady=5)

Sale4_frame = LabelFrame(shop_frame_sale, width=100, height=150, background='white')
Sale4_frame.grid(row=0, column=3,padx=5, pady=5)


#Sale_Product_Image_From_Sale1_to_Sale4
Sale1_label = Label(Sale1_frame,font=('Chalkduster',25), text='SALE1')
image = Image.open('SALE1.jpg')
resized_image = image.resize((255, 300))
Sale1_photo = ImageTk.PhotoImage(resized_image)
Sale1_image_label = Label(Sale1_frame, image=Sale1_photo, bg='white')
Sale1_price_label = Label(Sale1_frame, font=('Chalkduster',25), text='£20', bg='white')
Sale1_add_button = Button(Sale1_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('SALE1', '£20', counter))
Sale1_label.grid(row=0, column=0, padx=50,pady=30)
Sale1_image_label.grid(row=1, column=0, padx=45, pady=5)
Sale1_price_label.grid(row=2, column=0)
Sale1_add_button.grid(row=3, column=0)


Sale2_label = Label(Sale2_frame,font=('Chalkduster',25), text='SALE2')
image = Image.open('SALE2.jpg')
resized_image = image.resize((255, 300))
Sale2_photo = ImageTk.PhotoImage(resized_image)
Sale2_image_label = Label(Sale2_frame, image=Sale2_photo, bg='white')
Sale2_price_label = Label(Sale2_frame, font=('Chalkduster',25), text='£20', bg='white')
Sale2_add_button = Button(Sale2_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('SALE2', '£20', counter))
Sale2_label.grid(row=0, column=1, padx=50,pady=30)
Sale2_image_label.grid(row=1, column=1, padx=45, pady=5)
Sale2_price_label.grid(row=2, column=1)
Sale2_add_button.grid(row=3, column=1)


Sale3_label = Label(Sale3_frame,font=('Chalkduster',25), text='SALE3')
image = Image.open('SALE3.jpg')
resized_image = image.resize((260, 300))
Sale3_photo = ImageTk.PhotoImage(resized_image)
Sale3_image_label = Label(Sale3_frame, image=Sale3_photo, bg='white')
Sale3_price_label = Label(Sale3_frame, font=('Chalkduster',25), text='£20', bg='white')
Sale3_add_button = Button(Sale3_frame,font=('Chalkduster',25), text='ADD', command=lambda: add('SALE3', '£20', counter))
Sale3_label.grid(row=0, column=0, padx=50,pady=30)
Sale3_image_label.grid(row=1, column=0, padx=45, pady=5)
Sale3_price_label.grid(row=2, column=0)
Sale3_add_button.grid(row=3, column=0)


Sale4_label = Label(Sale4_frame,font=('Chalkduster',25), text='SALE4')
image = Image.open('SALE4.jpg')
resized_image = image.resize((260, 300))
Sale4_photo = ImageTk.PhotoImage(resized_image)
Sale4_image_label = Label(Sale4_frame, image=Sale4_photo, bg='white')
Sale4_price_label = Label(Sale4_frame, font=('Chalkduster',25), text='£20', bg='white')
Sale4_add_button = Button(Sale4_frame, font=('Chalkduster',25), text='ADD', command=lambda: add('SALE4', '£20', counter))
Sale4_label.grid(row=0, column=1, padx=50,pady=30)
Sale4_image_label.grid(row=1, column=1, padx=45, pady=5)
Sale4_price_label.grid(row=2, column=1)
Sale4_add_button.grid(row=3, column=1)


item_frame = Label(basket_frame, textvariable=basket_content, width=1000, font=('Chalkduster',27,'bold'))
item_frame.pack()



receipt_frame = LabelFrame(basket_frame, width=1400, height=1000, font=('Chalkduster',27,'bold'))
receipt_frame.pack()



root1.mainloop()