from pathlib import Path
import re,base64,io,json,hashlib
from PIL import Image,ImageOps,ImageDraw
root=Path('PA3/Use-Case Specification')
out=Path('tmp/image-audit');out.mkdir(parents=True,exist_ok=True)
rows=[]; thumbs=[]
for p in sorted(root.glob('*/*.md')):
 t=p.read_text(encoding='utf-8-sig'); clean=re.sub(r'^\[image\d+\]:.*$','',t,flags=re.M)
 imgs=re.findall(r'^\[(image\d+)\]: <data:image/[^;]+;base64,([^>]+)>',t,re.M)
 refs=re.findall(r'!\[[^\]]*\]\[(image\d+)\]',clean)
 name=p.stem; uc=re.search(r' -- (\d+) -- ',name).group(1)
 row={'uc':uc,'name':name,'path':str(p.resolve()),'images':len(imgs),'refs':len(refs),'text':clean,'hashes':[]}
 for label,b in imgs:
  raw=base64.b64decode(b); row['hashes'].append(hashlib.sha256(raw).hexdigest())
  im=Image.open(io.BytesIO(raw)).convert('RGB'); row.setdefault('sizes',[]).append(im.size)
  im.thumbnail((350,420)); tile=Image.new('RGB',(370,460),'#dddddd');tile.paste(im,((370-im.width)//2,30));ImageDraw.Draw(tile).text((8,8),f'UC-{uc} {label} {Image.open(io.BytesIO(raw)).size}',fill='black');thumbs.append(tile)
 rows.append(row)
for k in range(0,len(thumbs),12):
 sheet=Image.new('RGB',(370*4,460*3),'white')
 for n,im in enumerate(thumbs[k:k+12]):sheet.paste(im,((n%4)*370,(n//4)*460))
 sheet.save(out/f'contact-{k//12+1:02}.jpg')
(out/'audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'text.txt').write_text('\n\n'.join('===== '+r['name']+' IMAGES='+str(r['images'])+' =====\n'+r['text'] for r in rows),encoding='utf-8')
for r in rows:print(r['uc'],r['images'],r['refs'],r.get('sizes',[]),r['name'])
