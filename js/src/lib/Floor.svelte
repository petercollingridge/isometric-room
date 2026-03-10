<script>
  import Block from './Block.svelte';
  import { darkenHex, DX, DY } from '../utils';

  const {x, y, width1, width2, height, fill, floorBoardWidth} = $props();

  const dx = $derived(DX);
  const dy = $derived(DY);

  const positions = $derived.by(() => {
    const nBoards = 48 - floorBoardWidth;
    const boardWidth = width1 / nBoards;
    const out = [];
    for (let i = 1; i < nBoards; i++) {
      out.push([x - dx * i * boardWidth, y - 2 + dy * i * boardWidth]);
    }
    return out;
  });

</script>

<g>
  <Block x={x} y={y} width1={width1} width2={width2} height={10} fill="#ddd"/>
  <Block x={x} y={y - 2} width1={width1} width2={width2} height={height} fill={fill}/>
  {#each positions as [px, py], i (i)}
    <path d={`M${px},${py}l${dx * width2},${dy * width2}v${height}`} stroke={darkenHex(fill, 0.2)} stroke-width="1" fill="none"/>
  {/each}
</g>
