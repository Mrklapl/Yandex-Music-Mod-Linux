import os, sys

def patch_7511():
    path = "inspect_asar/app/_next/static/chunks/7511-470ddb0b1430b7fa.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We locate getData in module 35796
    target_start = "getData:(0,r.L3)(function*(n,l){let{context:d}=n"
    if target_start not in content:
        print("ERROR: target_start not found in 7511!")
        sys.exit(1)
        
    start_pos = content.find(target_start)
    end_marker = "}),S=n.default.default"
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        print("ERROR: end_marker not found in 7511!")
        sys.exit(1)
        
    old_block = content[start_pos:end_pos]
    print(f"Old block length: {len(old_block)}")
    
    new_block = """getData:(0,r.L3)(function*(n,l){let{context:d}=n;if(d&&d.type===s.b.WAVE&&Array.isArray(d.data?.seeds)){if(d.data.seeds.length===1&&d.data.seeds[0]==="user:onyourwave"){d={...d,data:{...d.data,seeds:["user:onyourwave","genre:all"]}}}}let u=(e=>{switch(e.type){case s.b.ALBUM:case s.b.ARTIST:return"".concat(e.type,":").concat(e.data.id);case s.b.PLAYLIST:return"".concat(e.type,":").concat(e.data.playlistUuid);case s.b.WAVE:return"".concat(e.type,":").concat(e.data.seeds.join(","));case s.b.GENERATIVE:case s.b.CLIP:return e.type;case s.b.OTHER:return"".concat(e.type,":").concat(e.data?.id??"")}})(d);if(u===e.lastRequestId&&e.items.length>0)return;let{wheelResource:m,modelActionsLogger:_}=(0,r._$)(e);e.loadingState=o.GuX.PENDING;let y=(()=>{if(0===i)return[];let e=Array(i),n=(a-i+100)%100;for(let a=0;a<i;a++){let i=t[(n+a)%100];i&&(e[a]=i)}return e})();let fbFn=e=>{let t=(e||(x=>x.id))({id:"vibe-wheel.activity-description"}),a=(e||(x=>x.id))({id:"vibe-wheel.mood-description"});return{wheelId:"PUMPKIN",items:[{id:"activity:wake-up",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-wake-up"}),description:t,seeds:["activity:wake-up"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/JVsyUlrs9Y",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-wake-up-agent-cover-RSUMc/%%",color:"#FFFFD6"}}}},{id:"activity:road-trip",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-road-trip"}),description:t,seeds:["activity:road-trip"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/Foah9sRLsS",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-activity-road-trip-agent-cover-S1vPp/%%",color:"#FFFFDF"}}}},{id:"activity:work-background",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-work-background"}),description:t,seeds:["activity:work-background"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/tsXpFHIBjM",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-work-background-agent-cover-5t6qb/%%",color:"#FFFFFF"}}}},{id:"activity:workout",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-workout"}),description:t,seeds:["activity:workout"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/PexWCCcEc9",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-workout-agent-cover-Wcrjo/%%",color:"#EBFFFE"}}}},{id:"activity:fall-asleep",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-fall-asleep"}),description:t,seeds:["activity:fall-asleep"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/J9QAoYnnPe",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-fall-asleep-agent-cover-XaOnj/%%",color:"#FAFFFF"}}}},{id:"mood:energetic",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-energetic"}),description:a,seeds:["mood:energetic"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/e6Ptlara08",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-energetic-agent-cover-NrJtV/%%",color:"#FDFAFF"}}}},{id:"mood:happy",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-happy"}),description:a,seeds:["mood:happy"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/EzOBeQmIXi",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-happy-agent-cover-JWFjr/%%",color:"#FFFFE8"}}}},{id:"mood:sad",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-sad"}),description:a,seeds:["mood:sad"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/rrF2I4tUvZ",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/30221/rotor-mood-sad-agent-cover-IN0O6/%%",color:"#EAFFFF"}}}}]};};try{let t=yield m.wheelNew({context:d,feedbacks:y});if(!t||!t.items||t.items.length===0){t=yield m.wheelNew({context:{type:s.b.WAVE,data:{seeds:["user:onyourwave","genre:all"]}},feedbacks:y})}let parsed=p(t);if(parsed&&parsed.length>0){i=0,e.wheelId=t.wheelId,e.items=(0,r.wg)(parsed),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else if(e.items.length===0){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else{e.loadingState=o.GuX.RESOLVE}})}})catch(t){if(_.error(t),e.isEmpty){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1}e.loadingState=o.GuX.RESOLVE}})}})"""
    
    patched_content = content[:start_pos] + new_block + content[end_pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched_content)
    print("Successfully patched 7511!")

def patch_6602():
    path = "inspect_asar/app/_next/static/chunks/6602.3894c4c5abbbd85d.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Patch 1: Desktop render fallback so it never collapses to empty
    target_render = "return l&&r?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    if target_render not in content:
        print("ERROR: target_render not found in 6602!")
        sys.exit(1)
    new_render = "return(l||r||0===i.length)?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    content = content.replace(target_render, new_render)
    
    # Patch 2: Add auto-fetch in G if empty
    target_effect = "(0,s.useEffect)(()=>{h()},[h]),(0,s.useEffect)(()=>{let e=p.current;e&&0!==i.length&&e.realIndex!==o&&(e.slideToLoop(o,0),Q(e))},[o,i.length]);"
    if target_effect not in content:
        print("ERROR: target_effect not found in 6602!")
        sys.exit(1)
    new_effect = "(0,s.useEffect)(()=>{h()},[h]),(0,s.useEffect)(()=>{let e=p.current;e&&0!==i.length&&e.realIndex!==o&&(e.slideToLoop(o,0),Q(e))},[o,i.length]),(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:[\"user:onyourwave\",\"genre:all\"]}}},_)}},[i.length]);"
    content = content.replace(target_effect, new_effect)
    
    # Patch 3: In entity change listener b
    target_case_vibe = "case _.K.Vibe:return{type:h.b.WAVE,data:{seeds:String(d).split(\",\")}};"
    if target_case_vibe not in content:
        print("ERROR: target_case_vibe not found in 6602!")
        sys.exit(1)
    new_case_vibe = "case _.K.Vibe:{let sd=String(d).split(\",\");if(sd.length===1&&sd[0]===\"user:onyourwave\")sd=[\"user:onyourwave\",\"genre:all\"];return{type:h.b.WAVE,data:{seeds:sd}}};"
    content = content.replace(target_case_vibe, new_case_vibe)
    
    # Patch 4: getData call condition in b
    target_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId)&&t.getData({context:l},e)"
    if target_call not in content:
        print("ERROR: target_call not found in 6602!")
        sys.exit(1)
    new_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId||t.isEmpty)&&t.getData({context:l},e)"
    content = content.replace(target_call, new_call)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched 6602!")

patch_7511()
patch_6602()
