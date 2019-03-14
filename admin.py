from flask import Flask, session, redirect, render_template, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import UsersModel, CarsModel, DealersModel
from forms import LoginForm, RegisterForm, AddCarForm, SearchPriceForm, SearchDealerForm, AddDealerForm
from db import DB

db = DB()

UsersModel(db.get_connection()).init_table()

def set_admin():
    users = UsersModel(db.get_connection())
    if "admin" in [u[1] for u in users.get_all()]:
        pass#print("admin already exists")
    else:
        users.insert(user_name="admin", email="andrewrogov@mail.ru", password_hash=generate_password_hash("superadmin"), credit_card="none", is_admin=1)
        
        
if __name__ == '__main__':
    set_admin()