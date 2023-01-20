<template>
    <div class="container my-5">
        <h2 class="text-center mb-5">Encounter Builder</h2>
        <form>
            <div class="form-group">
                <label for="number-of-enemies">Number of enemies:</label>
                <input type="number" class="form-control" id="number-of-enemies" v-model="numberOfEnemies"
                    placeholder="Enter Number of enemies">
            </div>
            <div class="form-group">
                <label for="enemy-type">Enemy Type:</label>
                <input type="text" class="form-control" id="enemy-type" v-model="enemyType"
                    placeholder="Enter Enemy Type">
            </div>
            <div class="form-group">
                <label for="environment">Environment:</label>
                <input type="text" class="form-control" id="environment" v-model="environment"
                    placeholder="Enter Environment">
            </div>
            <button class="btn btn-primary" v-on:click="generateEncounter()">Generate Encounter</button>
        </form>
    </div>
</template>
  
  
<script>
export default {
    data() {
        return {
            numberOfEnemies: '',
            enemyType: '',
            environment: '',
        }
    },
    methods: {
        generateEncounter() {
            // Use GPT-3 to generate text based on the input provided by the user
            // You can use axios or any other http library to call the GPT-3 API
            // and generate the text and then display it on the page
        }
    }
}
</script>
  
