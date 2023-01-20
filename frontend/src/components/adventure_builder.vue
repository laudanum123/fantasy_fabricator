<template>
  <div class="container my-5">
    <h2 class="text-center mb-5">Adventure Builder</h2>
    <form>
      <div class="form-group">
        <label for="adventure-title">Adventure Title:</label>
        <input type="text" class="form-control" id="adventure-title" v-model="adventureTitle"
          placeholder="Enter Adventure Title">
      </div>
      <div class="form-group">
        <label for="adventure-setting">Adventure Setting:</label>
        <input type="text" class="form-control" id="adventure-setting" v-model="adventureSetting"
          placeholder="Enter Adventure Setting">
      </div>
      <div class="form-group">
        <label for="adventure-plot">Adventure Plot:</label>
        <textarea class="form-control" id="adventure-plot" v-model="adventurePlot"
          placeholder="Enter Adventure Plot"></textarea>
      </div>
      <button class="btn btn-primary" v-on:click="generateAdventure()">Generate Adventure</button>
    </form>
  </div>
</template>


<script>
export default {
  data() {
    return {
      adventureTitle: '',
      adventureSetting: '',
      adventurePlot: '',
    }
  },
  methods: {
    generateAdventure() {
      // Use GPT-3 to generate text based on the input provided by the user
      // You can use axios or any other http library to call the GPT-3 API
      // and generate the text and then display it on the page
    }
  }
}
</script>
