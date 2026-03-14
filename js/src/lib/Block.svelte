<script>
  import { darkenHex, DX, DY } from '../utils';

  const {x, y, width1, width2, height, fill} = $props();

  const getTop = () => {
    const dx1 = DX * width1;
    const dy1 = DY * width1;
    const dx2 = DX * width2;
    const dy2 = DY * width2;
    return `M${x},${y}l${-dx1},${dy1} ${dx2},${dy2} ${dx1},${-dy1}z`;
  }

  const getLeftSide = () => {
    const x1 = x + DX * width2;
    const y1 = y + DY * width2;
    const dx = DX * width1;
    const dy = DY * width1;
    return `M${x1},${y1}v${height}l${-dx},${dy}v${-height}z`;
  }

  const getRightSide = () => {
    const x1 = x - DX * width1;
    const y1 = y + DY * width1;
    const dx = DX * width2;
    const dy = DY * width2;
    return `M${x1},${y1}v${height}l${dx},${dy}v${-height}z`;
  }

  const getStroke = (percentage) => {
    return darkenHex(fill, percentage);
  }

</script>

<g>
  <path d={getTop()} fill={fill} stroke={getStroke(0.2)}/>
  <path d={getLeftSide()} fill={getStroke(0.05)} stroke={getStroke(0.2)}/>
  <path d={getRightSide()} fill={getStroke(0.1)} stroke={getStroke(0.2)}/>
</g>
