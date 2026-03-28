# Rewrite Patterns

Use these patterns when converting a bloated skill into a progressive-disclosure skill.

## Pattern Matrix

| Symptom in `SKILL.md` | Rewrite | Preferred destination |
| --- | --- | --- |
| First-run welcome, setup tour, long onboarding copy | Keep detection + route only | `references/start.md` |
| Platform branches such as OpenClaw vs Claude Code vs Cursor | Replace prose with a compact decision table | `references/platform-variants.md` |
| Delivery, cron, language, hosting, export branches | Convert to pseudo-schema or decision matrix | `references/variants.md` |
| Full prompt copy or user speech templates | Keep intent constraints and placeholders in `SKILL.md`; move long samples out | `references/prompt-templates.md` |
| Repeated commands or shell blocks | Wrap into scripts when deterministic | `scripts/` |
| Long troubleshooting | Keep one-line failure routing in `SKILL.md`; move fixes out | `references/troubleshooting.md` |
| Many examples | Keep one template or parameter rule | `references/examples.md` |
| Mandatory full file reads | Add phase-based or branch-based read conditions | `SKILL.md` plus linked references |

## Preferred Compression Moves

### Onboarding to route-only

Before:
- several paragraphs of introduction
- a multi-question setup flow in `SKILL.md`

After:
- one line saying when onboarding is needed
- one link to `references/start.md`
- keep only the state-detection rule in `SKILL.md`

### Branch-heavy prose to table

Before:
- separate sections for Telegram, email, stdout, OpenClaw, cron, weekly, daily

After:
- one selection table
- one schema that lists the fields each branch needs
- branch-specific instructions moved into references

### Hardcoded speech to intent constraint

Before:
- full paragraphs beginning with "Tell the user:"

After:
- a short constraint such as "Explain the delivery tradeoff briefly and collect channel, cadence, and timezone."
- keep exact wording only if the behavior depends on that wording

### Examples to templates

Before:
- many expanded natural-language examples

After:
- one command template
- one argument-generation rule
- long examples moved into references if they still add unique value

### Repeated facts to invariant list

Before:
- the same warning repeated in several sections

After:
- one invariant list near the top
- later sections refer back to the invariant by name

## Default File Layout After Compression

```text
skill-name/
├── SKILL.md
├── references/
│   ├── start.md
│   ├── variants.md
│   ├── prompt-templates.md
│   └── troubleshooting.md
└── scripts/
    └── optional deterministic helpers
```

Do not create all of these files automatically. Create only the destinations a skill actually needs.
