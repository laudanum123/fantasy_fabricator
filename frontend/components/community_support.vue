<template>
  <div>
    <h1>Campaign Manager</h1>
    
    <input type="text" v-model="campaignName"/>
    <button @click="createCampaign()">Create Campaign</button>
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