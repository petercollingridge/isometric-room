<script>
  import { allItems } from '../assets/items.js';

  let {
    displayItems = $bindable(),
    floorColour = $bindable(),
    floorBoardWidth = $bindable()
  } = $props();

  function addItem(item) {
    console.log(item);
    displayItems.push({
      id: displayItems.length,
      x: 200,
      y: 300,
      width: item.width,
      height: item.height,
      scale: 1,
      href: `/src/assets/${item.img}.svg`,
    });
  }
</script>

<div class="sidebar">
  <section>
    <h3>Floor</h3>
    <div>
      <label>
        Colour:
        <input type="color" bind:value={floorColour}>
      </label>
    </div>
    <div>
      <label>
        Tile width:
        <input type="range" bind:value={floorBoardWidth} min={8} max={40}>
      </label>
    </div>
  </section>
  <section>
    <h3>Items</h3>
      {#each allItems as item (item.name)}
      <div class="item-name">{item.name}</div>
      <div class="item-img">
        <img src={`/src/assets/${item.img}.svg`} alt={item.img} width={item.width} height={item.height} />
      </div>
      <button onclick={() => addItem(item)}>Add</button>
      {/each}
  </section>
</div>

<style>
  section:not(:first-child) {
    margin-top: 1rem;
    border-top: 1px solid #ddd;
    padding-top: 0.5rem;
  }

  h3 {
    margin: 0;
  }

  section>div {
    margin-bottom: 0.5rem;
  }

  .item-img {
    padding: 5px;
    width: fit-content;
    border: 1px solid #ddd;
    margin: auto;
  }
</style>