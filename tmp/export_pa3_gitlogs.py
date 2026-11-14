from pathlib import Path
import subprocess,json
from datetime import datetime
from zoneinfo import ZoneInfo

root=Path.cwd(); output=root/'PA3/gitlog'; output.mkdir(parents=True,exist_ok=True)
configs=[('Backend','Backend-SWE','main'),('Frontend','Frontend-SWE','feature/user-profile-management'),('AI','AI-SWE','main')]
records=[]
def git(repo,*args):
    return subprocess.check_output(['git','--git-dir',str(repo),*args],encoding='utf-8')
for label,name,branch in configs:
    repo=root/'tmp/gitlog-pa3'/f'{name}.git'
    assert git(repo,'rev-parse','--is-shallow-repository').strip()=='false',name
    tip=git(repo,'rev-parse',f'refs/heads/{branch}').strip()
    hashes=git(repo,'rev-list',tip).splitlines()
    body=git(repo,'-c','i18n.logOutputEncoding=utf-8','log',tip,'--no-color','--no-decorate','--date=iso','--format=%h | %ad | %an | %s')
    dest=output/f'git_log_{label}.txt'
    dest.write_text(body,encoding='utf-8',newline='\n')
    lines=dest.read_text(encoding='utf-8').splitlines()
    assert len(lines)==len(hashes),(name,len(lines),len(hashes))
    assert len(set(hashes))==len(hashes)
    old=(root/f'PA2/gitlog/git_log_{label}.txt').read_text(encoding='utf-8-sig').splitlines()
    absent=[line.split(' | ')[0] for line in old if line.strip() and not any(h.startswith(line.split(' | ')[0]) for h in hashes)]
    roots=git(repo,'rev-list','--max-parents=0',tip).splitlines()
    record={'repository':f'https://github.com/Adiff-git/{name}','branch':branch,'head':tip,'commit_count':len(hashes),'root_commits':roots,'shallow':False,'pa2_missing_commits':absent,'latest_entry':lines[0],'oldest_entry':lines[-1],'file':dest.name}
    records.append(record)
    print(json.dumps(record,ensure_ascii=False))
stamp=datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds')
(output/'verification.json').write_text(json.dumps({'exported_at':stamp,'repositories':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
readme=['# PA3 Git logs','',f'Exported at: {stamp} (Asia/Ho_Chi_Minh).','',
'Same TXT layout as PA2: `short hash | author date and original timezone | author name | subject`. Newest entries are shown first using Git default ordering. Includes all commits reachable from the selected branch head, including merge commits and merged branch history. No date filter, shallow clone, first-parent restriction, or commit-count limit was used. Commits exclusive to unrelated/unmerged branches are outside these branch-specific logs.','',
'| File | Repository / branch | Commits | Head SHA |','| --- | --- | ---: | --- |']
for r in records:
    readme.append(f'| [{r["file"]}]({r["file"]}) | [{r["repository"].split("/")[-1]} / {r["branch"]}]({r["repository"]}/tree/{r["branch"]}) | {r["commit_count"]} | `{r["head"]}` |')
readme+=['','Reproduction (after fetching the selected branch without `--depth`):','',
'```text','git log <head-sha> --no-color --no-decorate --date=iso --format="%h | %ad | %an | %s"','```','',
'Checks: each repository is non-shallow; exported row counts match `git rev-list --count <head-sha>`; no duplicate full commit hashes; root commits are present. `verification.json` records each immutable head, root commits, counts, and comparison against PA2.']
for r in records:
    readme.append(f'- {r["repository"].split("/")[-1]}: '+('all PA2 commit hashes are included.' if not r['pa2_missing_commits'] else 'PA2 hashes not reachable from this selected branch: '+', '.join(r['pa2_missing_commits'])))
(output/'README.md').write_text('\n'.join(readme)+'\n',encoding='utf-8')
