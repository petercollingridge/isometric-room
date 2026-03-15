<script>
  import { allItems } from '../assets/items.js';

  let {
    displayItems = $bindable(),
    floorColour = $bindable(),
    floorBoardWidth = $bindable(),
    selected = $bindable(),
  } = $props();

  function addItem(item) {
    const itemData = {...item};
    itemData.id = displayItems.length;
    itemData.x = 200;
    itemData.y = 200;
    itemData.flip = false;
    itemData.href = `/src/assets/${item.img}.svg`;

    displayItems.push(itemData);
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

  {#if selected}
    <section>
      <h3>Selected item</h3>
      <div>{selected.item.name}</div>
      <div>
        <label>
          x:
          <input class="coord-input" type="number" bind:value={selected.item.x}>
        </label>
        <label>
          y:
          <input class="coord-input" type="number" bind:value={selected.item.y}>
        </label>
      </div>
      <div>
        <label>
          Flip:
          <input type="checkbox" bind:checked={selected.item.flip}>
        </label>
      </div>
    </section>
  {/if}

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

  .coord-input {
    width: 100px;
    margin-right: 10px;
  }
</style>