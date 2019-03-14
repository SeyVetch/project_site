from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email
#from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

#images = UploadSet('images', IMAGES)


class LoginForm(FlaskForm):
    """Форма авторизации"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    card = StringField('Кредитная карточка', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение', validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddCarForm(FlaskForm):
    """Форма добавления автомобиля"""
    model = StringField('Имя', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    power = IntegerField('Мощность (л.с.)', validators=[DataRequired()])
    dealer_id = SelectField('Номер породы', coerce=int, validators=[DataRequired()])
    #image = FileField('image', validators=[
    #        #FileRequired(),
    #        FileAllowed(['jpg', 'png'], 'Images only!')
    #    ])    
    submit = SubmitField('Добавить коня')


class AddDealerForm(FlaskForm):
    """Добавление дилерского центра"""
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес фермы', validators=[DataRequired()])
    submit = SubmitField('Добавить породу')


class SearchPriceForm(FlaskForm):
    """Форма поиска по цене"""
    start_price = IntegerField('Минимальная цена', validators=[DataRequired()], default=500000)
    end_price = IntegerField('Максимальная цена', validators=[DataRequired()], default=1000000)
    submit = SubmitField('Поиск')


class SearchDealerForm(FlaskForm):
    """Форма поиска по дилерскому центру"""
    dealer_id = SelectField('Номер дилерского центра', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Поиск')
