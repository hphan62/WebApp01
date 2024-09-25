import streamlit as st
from modules import todosUtil

def add_task():
    ''' add task to todos list '''
    my_task = st.session_state['new_task'] + '\n'
    todos.append(str.capitalize(my_task))
    todosUtil.save_todos(todos)


# Page Title
st.title('My Todo Web App')
st.subheader('This my todo app')
st.write('This app help you to increase your productivity.')

# Loading current tasks
todos = todosUtil.get_todos()

# Rendering tasks to webpage
for idx, task in enumerate(todos):
    # add check box dynamically and each has its own key
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        #print(checkbox)
        # remove task from todos list
        todos.pop(idx)
        # save the todos list
        todosUtil.save_todos(todos)
        # remove the task from current session
        del st.session_state[task]
        # run it again
        st.rerun()

# Rendering Input textbox
st.text_input(label='Enter new task:', placeholder='Enter task ...',
              on_change=add_task, key='new_task'
              )
