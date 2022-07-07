function classToggle() {
    const sidebars = document.querySelectorAll('.account_lists');
    sidebars.forEach(nav => nav.classList.toggle('account_lists_show'));
    
    document.querySelector(".my_account_details").classList.toggle('d-none')

}

const details = document.querySelector('.Navbar__Link-toggle');
details.addEventListener('click', classToggle)
