# imagery.md — the repertoire rules

Metaphors, analogies, and memes are how classic style *shows*. They are too
powerful to improvise. This file governs how they are chosen at stage 02 and
written at stage 03. The law in one line (`rules.md §imagery-and-visuals`):
**nothing off the map appears in the draft.** Stage 02 draws the map; stage 03
may use it and may not exceed it.

## 1. One controlling metaphor per piece

A piece gets a single controlling metaphor — the spine image the reader can hold
the whole way through. It is drawn from **the audience's own world**, named in
their profile's §4 source domain. The comic fan gets continuity and retcons; the
child gets playground physics; the tradesperson gets the job site. Borrowing the
audience's domain is what makes the image feel like recognition rather than
instruction.

## 2. Supporting images must be complementary

Secondary analogies must live in the **same source domain** as the controlling
metaphor, or in a domain explicitly declared compatible with it on the map.
Complementarity is a rule, not a hope: a piece whose images come from four
unrelated worlds reads as clutter, and mixed metaphors are flagged as defects at
stage 04. One coherent world, extended.

## 3. Layering: unfold the metaphor with the argument

For complex topics the controlling metaphor is **layered**, not front-loaded.
Introduce it at its simplest where the argument is simplest — early — then
*extend* it as the complexity grows. It is extended, never replaced: the reader
who grasped the simple version finds the harder version waiting inside it. The
image should unfold at the same rate as the text, so that the metaphor and the
understanding arrive together.

## 4. The condescension test (gates everything)

Before any image makes the map, ask: **would a member of this audience use this
image among themselves?** An image that explains their own world back to them,
or that an outsider would reach for to seem relatable, fails. This is the same
test the audience profiles state in their §5 — it lives here too because imagery
is where condescension most often sneaks in. The respect floor
(`rules.md §respect-floor`) outranks any clever image.

## 5. Memes — licensed jointly, listed like everything else

A meme is just another image and obeys every rule above, plus two more:
- **Licensed by format AND audience jointly.** Reddit + a meme-fluent audience:
  yes. Op-ed: no, whatever the audience. The format file's §6 and the audience's
  tolerance must *both* permit it.
- **Evergreen over topical.** A meme that will read as dated next year is a
  liability; prefer ones that have earned permanence.
A licensed meme goes on the imagery map like any other image. A meme not on the
map does not appear in the draft.

## 6. The imagery map (stage 02's output block)

Stage 02 writes an `## Imagery` block into `outline.md`:

```
## Imagery
- Controlling metaphor: <metaphor> — source domain: <from audience §4>
- Layering: <how it's introduced simply, then extended; which beats deepen it>
- Supporting images:
  - <image A> → serves beat <n>  (domain: same / compatible: <name>)
  - <image B> → serves beat <m>
- Memes: <licensed meme + beat, or "none — not licensed by format/audience">
- Condescension check: <one line confirming each image passes §4>
```

Every image names the beat it serves. Stage 03 writes these images and **no
others**; stage 04 checks the draft's images against this map and flags any that
are mixed, orphaned (no beat), or absent from the map.
