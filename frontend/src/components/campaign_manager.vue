<template>
  <div class="container my-5">
    <h2 class="text-center mb-5">Campaign Manager</h2>
    <div class="form-group">
      <input type="text" class="form-control" v-model="campaignName" placeholder="Enter campaign name">
    </div>
    <button class="btn btn-primary" @click="createCampaign()">Create Campaign</button>
  </div>
</template>


<script>
export default {
  data() {
    return {
      campaignName: ''
    }
  },
  methods: {
    createCampaign() {
      // Send AJAX request to backend with campaign name
    }
  }
}
</script>