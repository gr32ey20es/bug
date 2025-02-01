# No[e]

## Question

    Remote code execution?
    Variable reordering: Why do they not copy ret_addr like arg?

## Answer

    No[e]

## Keyword

    GS.Stack cookie: random value, overwrite ret_addr --> change cookie's value

    #pragma strict_gs_check: minimize the perf impact

    Variable reordering: prevent from overwriting local var/arg

    SafeSEH: header contains a table of all valid exception handlers within that module
    