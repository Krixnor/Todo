// script.js

// alert("Created By KrixCode");




let taskForm = document.querySelector('#task-form')
let task = document.querySelector('#title').value 
let taskList = document.querySelector('#tasks');

fetch("{% url 'task-list' %}")
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        
        .then(data => {
            let taskContainer = document.querySelector('#tasksContainer')
            data.forEach(element => {
                
                let tasksItem = document.createElement('li');
                tasksItem.innerHTML = element.title;
                taskContainer.appendChild(tasksItem)
            });
            
           
            console.log(data)
        })
        .catch(error => {
            console.log("Error:", error);
        });
































//     let taskForm = document.querySelector('#task-form')
//     let task = document.querySelector('#title').value 
//     console.log(task)
//     taskForm.addEventListener('submit', (e)=>{
//         e.preventDefault()
//         fetch("/new/",{
//             method:"POST",
//             headers: {
//                 "Content-Type": "application/json",
//                 "X-CSRFToken":csrftoken
//             },
//             body: JSON.stringify({'title':task})
//         })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error("Network response was not ok");
//             }
//             return response.json();
//         })
//         .then(data => {
//             let taskList = document.querySelector('#tasks');
//             let tasksItem = document.createElement('li');
//             tasksItem.textContent = data.title;
//             console.log('good')
//         })
//         .catch(error => {
//             console.log("Error:", error);
//         });
    
//     })

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');











// document.addEventListener('DOMContentLoaded', function () {

//     document.querySelector('#submit').disabled = true;
//     document.querySelector('#submit').style.background = 'grey'

//     document.querySelector('#task').onkeyup = () => {
//         if (document.querySelector('#task').value.length > 0) {
//             document.querySelector('#submit').disabled = false;
//             document.querySelector('#submit').style.background = 'teal'
//         } else {
//             document.querySelector('#submit').disabled = true;
//             document.querySelector('#submit').style.background = 'grey'
//         }

//     }

    // document.querySelector('form').onsubmit = () => {
        // e.preventDefault()
        // const task = document.querySelector('#task').value;
        // const list = document.createElement('li');
        // const tweak = document.createElement('div')
        // const para = document.createElement('p')
        // const deleteButton = document.createElement('button');
        // const editButton = document.createElement('button');
        // deleteButton.innerHTML = '❌'; // You can use any symbol or text for the delete button
        // editButton.innerHTML = '<small>edit </small>'
        
        // deleteButton.onclick = function () {
        //     list.remove();
        // };

        // editButton.onclick = function () {
        //     const tempTextContent = list.textContent.trim();
        //     const editedTask = prompt("Edit your task:", tempTextContent);
        //     if (editedTask !== null && editedTask.trim() !== "") {
        //         list.textContent = editedTask;
        //     }
        // };

//         para.innerHTML = task;
//         list.appendChild(para);
//         list.appendChild(tweak);
//         tweak.appendChild(deleteButton)
//         tweak.appendChild(editButton);
//         document.querySelector('ul').append(list);

//         document.querySelector('#task').value = ''
//         document.querySelector('#submit').disabled = true;
       
//         return true;

//     }
// });
