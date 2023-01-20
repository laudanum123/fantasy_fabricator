<template>
  <div class="container my-5">
    <h2 class="text-center mb-5">Community Support</h2>
    <div class="form-group">
      <label for="campaign-name">Campaign Name:</label>
      <input type="text" class="form-control" id="campaign-name" v-model="campaignName"
        placeholder="Enter Campaign Name">
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