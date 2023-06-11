btnModals = document.querySelectorAll('.open-modal-btn');

btnModals.forEach(btnModal => {
    btnModal.onclick = () => {
        modal = document.querySelector(btnModal.dataset.modalid)

        modal.classList.add('modal-show')
        modalContent = document.querySelector(`${
            btnModal.dataset.modalid
        } .modal-content`)
        modalContent.style.animation = 'modalOpen .5s forwards'
        closeBtn = document.querySelector(`${
            btnModal.dataset.modalid
        } .close-modal-btn`)
        closeBtn.onclick = () => modal.classList.remove('modal-show')
    }
})
