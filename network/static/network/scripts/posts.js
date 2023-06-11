editBtns = document.querySelectorAll('.editBtn')

editBtns.forEach(editBtn => {

    editBtn.onclick = () => {

        document.querySelector('#post' + editBtn.dataset.postid).style.display = 'none'
        document.querySelector('#post' + editBtn.dataset.postid + 'edit').style.display = 'block'
        textarea = document.querySelector('#post' + editBtn.dataset.postid + 'edit' + ' textarea')
        textarea.selectionStart = textarea.selectionEnd = textarea.value.length
        textarea.focus()
    }
})

cancelBtns = document.querySelectorAll('.cancelBtn')

cancelBtns.forEach(cancelBtn => {
    cancelBtn.onclick = () => {
        document.querySelector('#post' + cancelBtn.dataset.postid).style.display = 'block'
        document.querySelector('#post' + cancelBtn.dataset.postid + 'edit').style.display = 'none'
    }
})

saveBtns = document.querySelectorAll('.saveBtn')

saveBtns.forEach(saveBtn => {
    csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value

    saveBtn.onclick = () => {
        text = document.querySelector('#post' + saveBtn.dataset.postid + 'edit' + ' textarea').value
        fetch('/' + saveBtn.dataset.postid, {
            method: 'PATCH',
            headers: {
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({text})
        }).then(response => response.json()).then(result => {

            document.querySelector('#post' + saveBtn.dataset.postid).style.display = 'block'
            document.querySelector('#post' + saveBtn.dataset.postid + 'edit').style.display = 'none'
            document.querySelector('#post' + saveBtn.dataset.postid + ' p').innerText = result.updated_text
        })

    }
})

likeBtns = document.querySelectorAll('.like-btn')

likeBtns.forEach(likeBtn => {
    likeBtn.onclick = () => {
        fetch('/' + likeBtn.dataset.postid, {
            method: 'PATCH',
            headers: {
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(
                {toogle_like: true}
            )
        }).then(response => response.json()).then(result => {

            if (result.liked) {
                likeBtn.innerHTML = `Unlike <span class="like-counter">(${
                    result.likers
                })</span>`
            } else {
                likeBtn.innerHTML = `Like <span class="like-counter">(${
                    result.likers
                })</span>`
            }
        }).catch(error => print(error))
    }
})
