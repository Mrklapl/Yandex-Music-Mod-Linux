import os, sys

def patch_7511(inspect_dir):
    path = os.path.join(inspect_dir, "app/_next/static/chunks/7511-470ddb0b1430b7fa.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Locate getData in module 35796
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
        
    # Clean getData block without forcing genre:all, perfectly balanced syntax
    new_block = """getData:(0,r.L3)(function*(n,l){let{context:d}=n;let u=(e=>{switch(e.type){case s.b.ALBUM:case s.b.ARTIST:return"".concat(e.type,":").concat(e.data.id);case s.b.PLAYLIST:return"".concat(e.type,":").concat(e.data.playlistUuid);case s.b.WAVE:return"".concat(e.type,":").concat(e.data.seeds.join(","));case s.b.GENERATIVE:case s.b.CLIP:return e.type;case s.b.OTHER:return"".concat(e.type,":").concat(e.data?.id??"")}})(d);if(u===e.lastRequestId&&e.items.length>0)return;let{wheelResource:m,modelActionsLogger:_}=(0,r._$)(e);e.loadingState=o.GuX.PENDING;let y=(()=>{if(0===i)return[];let e=Array(i),n=(a-i+100)%100;for(let a=0;a<i;a++){let i=t[(n+a)%100];i&&(e[a]=i)}return e})();let fbFn=e=>{let t=(e||(x=>x.id))({id:"vibe-wheel.activity-description"}),a=(e||(x=>x.id))({id:"vibe-wheel.mood-description"});return{wheelId:"PUMPKIN",items:[{id:"activity:wake-up",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-wake-up"}),description:t,seeds:["activity:wake-up"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/JVsyUlrs9Y",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-wake-up-agent-cover-RSUMc/%%",color:"#FFFFD6"}}}},{id:"activity:road-trip",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-road-trip"}),description:t,seeds:["activity:road-trip"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/Foah9sRLsS",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-activity-road-trip-agent-cover-S1vPp/%%",color:"#FFFFDF"}}}},{id:"activity:work-background",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-work-background"}),description:t,seeds:["activity:work-background"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/tsXpFHIBjM",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-work-background-agent-cover-5t6qb/%%",color:"#FFFFFF"}}}},{id:"activity:workout",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-workout"}),description:t,seeds:["activity:workout"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/PexWCCcEc9",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/2413828/rotor-activity-workout-agent-cover-Wcrjo/%%",color:"#EBFFFE"}}}},{id:"activity:fall-asleep",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.activity-fall-asleep"}),description:t,seeds:["activity:fall-asleep"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/J9QAoYnnPe",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/28592/rotor-activity-fall-asleep-agent-cover-XaOnj/%%",color:"#FAFFFF"}}}},{id:"mood:energetic",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-energetic"}),description:a,seeds:["mood:energetic"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/e6Ptlara08",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-energetic-agent-cover-NrJtV/%%",color:"#FDFAFF"}}}},{id:"mood:happy",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-happy"}),description:a,seeds:["mood:happy"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/EzOBeQmIXi",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/70683/rotor-mood-happy-agent-cover-JWFjr/%%",color:"#FFFFE8"}}}},{id:"mood:sad",type:c.D.WAVE,data:{wave:{name:(e||(x=>x.id))({id:"vibe-wheel.mood-sad"}),description:a,seeds:["mood:sad"]},agent:{animationUri:"https://music-custom-wave-media.music.yandex.net/rrF2I4tUvZ",cover:{uri:"https://avatars.mds.yandex.net/get-music-misc/30221/rotor-mood-sad-agent-cover-IN0O6/%%",color:"#EAFFFF"}}}}]};};try{let t=yield m.wheelNew({context:d,feedbacks:y});let parsed=p(t);if(parsed&&parsed.length>0){i=0,e.wheelId=t.wheelId,e.items=(0,r.wg)(parsed),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else if(e.items.length===0){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1,e.lastRequestId=u,e.loadingState=o.GuX.RESOLVE}else{e.loadingState=o.GuX.RESOLVE}}catch(t){if(_.error(t),e.isEmpty){let fb=fbFn(l);e.wheelId=fb.wheelId,e.items=(0,r.wg)(p(fb)),e.activeIndex=1}e.loadingState=o.GuX.RESOLVE}})}"""
    
    content = content[:start_pos] + new_block + content[end_pos:]
    
    # 2. Fix null-safe addFeedback calls to prevent Uncaught TypeError in detached items
    target_fb_view = "handleFeedbackView(){let{wheel:t}=(0,r.Zn)(e);t.addFeedback(i.VIEW,e.type,e.id,e.index)}"
    safe_fb_view = "handleFeedbackView(){let t=(0,r.Zn)(e);(t?.wheel||t)?.addFeedback?.(i.VIEW,e.type,e.id,e.index)}"
    if target_fb_view in content:
        content = content.replace(target_fb_view, safe_fb_view)
        
    target_fb_click = "handleFeedbackClick(){let{wheel:t}=(0,r.Zn)(e);t.addFeedback(i.CLICK,e.type,e.id,e.index)}"
    safe_fb_click = "handleFeedbackClick(){let t=(0,r.Zn)(e);(t?.wheel||t)?.addFeedback?.(i.CLICK,e.type,e.id,e.index)}"
    if target_fb_click in content:
        content = content.replace(target_fb_click, safe_fb_click)
        
    # 3. Add PROMO support to enum module 58412 (used by BaseWheelItem style validation)
    target_enum = 'e.DEFAULT="DEFAULT",e.CONTROL="CONTROL",e.CONTROL_ACCENT="CONTROL_ACCENT"'
    new_enum = 'e.DEFAULT="DEFAULT",e.CONTROL="CONTROL",e.CONTROL_ACCENT="CONTROL_ACCENT",e.PROMO="PROMO"'
    if target_enum in content:
        content = content.replace(target_enum, new_enum)
        
    # 4. Normalize style fallback in module 35796 p function
    target_p_style = "style:e.style??d.y.DEFAULT"
    new_p_style = "style:(e.style&&Object.values(d.y).includes(e.style))?e.style:d.y.DEFAULT"
    if target_p_style in content:
        content = content.replace(target_p_style, new_p_style)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched 7511!")

def patch_6602(inspect_dir):
    path = os.path.join(inspect_dir, "app/_next/static/chunks/6602.3894c4c5abbbd85d.js")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Desktop render fallback so it never collapses to empty
    target_render = "return l&&r?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    new_render = "return(l||r||0===i.length)?(0,a.jsx)(H,{className:t}):(0,a.jsx)(v.RC,"
    if target_render in content:
        content = content.replace(target_render, new_render)
    
    # 2. In entity change listener b: restore genuine seeds (remove genre:all hack)
    hack_case_vibe = 'case _.K.Vibe:{let sd=String(d).split(",");if(sd.length===1&&sd[0]==="user:onyourwave")sd=["user:onyourwave","genre:all"];return{type:h.b.WAVE,data:{seeds:sd}}};'
    clean_case_vibe = 'case _.K.Vibe:return{type:h.b.WAVE,data:{seeds:String(d).split(",")}};'
    if hack_case_vibe in content:
        content = content.replace(hack_case_vibe, clean_case_vibe)
    
    # 3. Clean any illegal hook calls in G
    bad_effects = [
        ';(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}},_)}},[i.length]);',
        '(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}},_)}},[i.length]);',
        ';(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave","genre:all"]}}},_)}},[i.length]);',
        '(0,s.useEffect)(()=>{if(0===i.length){(0,c.Pjs)().wheel.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave","genre:all"]}}},_)}},[i.length]);'
    ]
    for b in bad_effects:
        content = content.replace(b, "")
    
    # Ensure semicolon after slideToLoop effect closing parenthesis before let j
    content = content.replace("},[o,i.length])let j=", "},[o,i.length]);let j=")
    content = content.replace("},[o,i.length]),let j=", "},[o,i.length]);let j=")
    
    # 4. In he: add safe on-mount check to trigger wheel fetch if empty
    target_he_effect = '(0,s.useEffect)(()=>{let e=p?.state.queueState.currentEntity.onChange(b);return()=>{null==e||e()}},[p,b,i])'
    new_he_effect = '(0,s.useEffect)(()=>{if(i.isEmpty){let cur=p?.state?.queueState?.currentEntity?.value;cur?b(cur):i.getData({context:{type:h.b.WAVE,data:{seeds:["user:onyourwave"]}}})}let e=p?.state.queueState.currentEntity.onChange(b);return()=>{null==e||e()}},[p,b,i])'
    if target_he_effect in content:
        content = content.replace(target_he_effect, new_he_effect)
    
    # 5. getData call condition in b: allow getData if isEmpty
    target_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId)&&t.getData({context:l},e)"
    new_call = "(i.entityMeta?.isTrackMusic||!t.lastRequestId||t.isEmpty)&&t.getData({context:l},e)"
    if target_call in content:
        content = content.replace(target_call, new_call)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched 6602!")

if __name__ == "__main__":
    inspect_dir = sys.argv[1] if len(sys.argv) > 1 else "inspect_asar"
    if not os.path.isdir(inspect_dir):
        # Check parent directory
        if os.path.isdir(os.path.join("..", inspect_dir)):
            inspect_dir = os.path.join("..", inspect_dir)
        else:
            print(f"ERROR: {inspect_dir} not found!")
            sys.exit(1)
    print(f"Applying wheel patch to: {inspect_dir}")
    patch_7511(inspect_dir)
    patch_6602(inspect_dir)
    print("All patches applied successfully!")
