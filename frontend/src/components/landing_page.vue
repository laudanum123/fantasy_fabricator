<template>
  <div class="container my-5">
    <!-- Hero Section -->
    <div class="jumbotron text-center">
      <h1 class="display-4">Welcome to Fantasy Fabricator</h1>
      <p class="lead">Become the ultimate dungeon master with Fantasy Fabricator, where AI-generated adventures,
        characters, and enemies await</p>
      <p class="text-muted">Say goodbye to writer's block and hello to endless possibilities with Fantasy Fabricator.
        Our AI-powered tool generates unique and exciting adventure ideas, detailed and compelling characters, and
        terrifying and challenging enemies. Take your campaigns to the next level with Fantasy Fabricator.</p>
      <hr class="my-4">
    </div>

    <!-- Features Section -->
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Create Adventures</h5>
            <p class="card-text">Use GPT-3 to generate unique and exciting adventure ideas.</p>
            <router-link to="/adventures" class="btn btn-primary">Create Adventure</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Create Characters</h5>
            <p class="card-text">Use GPT-3 to generate detailed and compelling characters.</p>
            <router-link to="/characters" class="btn btn-primary">Create Character</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Create Enemies</h5>
            <p class="card-text">Use GPT-3 to generate terrifying and challenging enemies.</p>
            <router-link to="/enemies" class="btn btn-primary">Create Enemy</router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="row my-5">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Campaign Manager</h5>
            <p class="card-text">Manage and organize your campaigns, keep track of characters, and plan out adventures.
            </p>
            <router-link to="/campaigns" class="btn btn-primary">Manage Campaigns</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Map Generator</h5>
            <p class="card-text">Use GPT-3 to generate detailed and unique maps for your campaigns.</p>
            <router-link to="/maps" class="btn btn-primary">Create Map</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Community Support</h5>
            <p class="card-text">Connect with other Dungeon Masters and get tips and support.</p>
            <router-link to="/community" class="btn btn-primary">Join Community</router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="row my-5">
      <div class="col-md-12 text-center">
        <h2>Why Use Fantasy Fabricator?</h2>
        <p>Fantasy Fabricator utilizes the power of AI to revolutionize the way you create and manage your RPG
          campaigns. Say goodbye to hours spent on coming up with unique adventure ideas or creating detailed characters
          - our AI-generated content will give you endless possibilities for your campaigns. Plus, our campaign manager
          feature allows for easy organization and planning, and our community support feature connects you with other
          dungeon masters for tips and support. Fantasy Fabricator is the ultimate tool for any dungeon master.</p>
      </div>
    </div>
  </div>
</template>
