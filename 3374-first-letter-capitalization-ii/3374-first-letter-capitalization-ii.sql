# Write your MySQL query statement below
-- Split every string into one character per row
WITH RECURSIVE cte AS (
    SELECT
        content_id,
        content_text,
        LENGTH(content_text) AS len
    FROM user_content
),

chars AS (
    SELECT      -- anchor
        content_id,
        1 AS pos,
        LOWER(SUBSTRING(content_text,1,1)) AS ch,
        LOWER(content_text) AS txt,
        len,
        0 AS word_idx
    FROM cte

    UNION ALL

    SELECT      -- recursive member
        content_id,
        pos + 1,
        LOWER(SUBSTRING(txt,pos+1,1)),
        txt,
        len,
        -- increment word_idx when current char is space
        word_idx + CASE WHEN ch = ' ' THEN 1 ELSE 0 END
    FROM chars
    WHERE pos < len
),

-- For each word, check if it has exactly 1 '-' 
-- AND '-' is not at position 1 of that word
word_info AS (
    SELECT 
        content_id,
        word_idx,
        SUM(CASE WHEN ch = '-' THEN 1 ELSE 0 END) AS hyphen_count,
        MIN(pos) AS word_start_pos, -- first position of word
        MIN(CASE WHEN ch = '-' THEN pos ELSE NULL END) 
        AS first_hyphen_pos -- position of first '-'
        -- '-' is leading if it appears at 1st position of the word
        -- (word_start_pos <> first_hyphen+pos) [TO CHECK]
    FROM chars c
    GROUP BY content_id, word_idx
)

-- Reconstruct Sentence (FINAL)
SELECT
    c.content_id,
    MAX(u.content_text) AS original_text,
    GROUP_CONCAT(
        CASE
            -- First character
            WHEN c.pos = 1
                THEN UPPER(c.ch)

            -- Previous character is space
            WHEN SUBSTRING(c.txt, c.pos-1, 1) = ' '
                THEN UPPER(c.ch)

            -- (Previous char is '-') AND (word has exactly 1 '-'), 
            -- AND (that '-' is NOT Leading the word)
            WHEN SUBSTRING(c.txt, c.pos-1, 1) = '-'
                AND wi.hyphen_count = 1
                AND wi.first_hyphen_pos <> wi.word_start_pos
                THEN UPPER(c.ch)

            -- Everything else remains lowercase
            ELSE c.ch
        END 
        ORDER BY c.pos
        SEPARATOR ''
    ) AS converted_text
FROM chars c
JOIN user_content u 
    ON c.content_id = u.content_id
JOIN word_info wi 
    ON c.content_id = wi.content_id AND c.word_idx = wi.word_idx
GROUP BY c.content_id
ORDER BY c.content_id;