<template>
  <div>
    <input v-model="newTodo" @keyup.enter="addTodo" >
    <ul>
      <li v-for="(todo, index) in todos" :key="todo.id">
        <span>{{ todo.text }}</span>
        <button @click="removeTodo(index)">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: "",
      todos: [{ text: "TODOを追加してください" }]
    }
  },
  methods: {
    addTodo() {
      var text = this.newTodo.trim()
      if (text) {
        this.todos.push({ text: text })
        this.newTodo = ""
      }
    },
    removeTodo(index) {
      this.todos.splice(index, 1)
    }
  }
}
</script>
