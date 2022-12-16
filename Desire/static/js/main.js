// Выезжающая панель справа

$(function () {

    $('.header__btn').on('click', function () {
        $('.rightside-menu').removeClass('rightside-menu--close');
    });
    $('.rightside-menu__close').on('click', function () {
        $('.rightside-menu').addClass('rightside-menu--close');
    });

    $('.header__btn-menu').on('click', function () {
        $('.menu').toggleClass('menu--open');
    });

    if($(window).width() < 651){
        $('.works-path__item--measuring').appendTo($('.works-path__items-box'));
    }

    var mixer = mixitup('.gallery__inner' , {
        load: {
            filter: '.living'
        }
    });


})


const openPopUpInput = document.getElementById('open_pop_up_input');
const closePopUpInput = document.getElementById('pop_up_close_input');
const popUpInput = document.getElementById('pop_up_input');

openPopUpInput.addEventListener('click', function(e){
    e.preventDefault();
    popUpInput.classList.add('active');
})

closePopUpInput.addEventListener('click', () => {
    popUpInput.classList.remove('active');
})


const openPopUpReg = document.getElementById('open_pop_up_reg');
const closePopUpReg = document.getElementById('pop_up_close_reg');
const popUpReg = document.getElementById('pop_up_reg');

openPopUpReg.addEventListener('click', function(e){
    e.preventDefault();
    popUpReg.classList.add('active');
})

closePopUpReg.addEventListener('click', () => {
    popUpReg.classList.remove('active');
})