<template>
    <div>
        <form>
            <label for="number-of-enemies">Number of enemies:</label>
            <input type="number" id="number-of-enemies" v-model="numberOfEnemies" placeholder="Enter Number of enemies">
            <br><br>
            <label for="enemy-type">Enemy Type:</label>
            <input type="text" id="enemy-type" v-model="enemyType" placeholder="Enter Enemy Type">
            <br><br>
            <label for="environment">Environment:</label>
            <input type="text" id="environment" v-model="environment" placeholder="Enter Environment">
            <br><br>
            <button v-on:click="generateEncounter()">Generate Encounter</button>
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
  
