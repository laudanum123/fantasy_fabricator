<template>
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">{{ title }}</h4>
        <p class="card-text"><slot></slot></p>
      </div>
    </div>
    <br>
  </template>
  
  <script>
  export default {
    name: 'MyCard',
    props: {
      title: {
        type: String,
        required: true
      }
    }
  }
  </script>
  

<style scoped>
.card {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

.card:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}
</style>