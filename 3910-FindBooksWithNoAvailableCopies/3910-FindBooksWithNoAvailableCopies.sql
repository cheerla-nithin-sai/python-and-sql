-- Last updated: 4/20/2026, 1:24:10 PM
# Write your MySQL query statement below
with cte as (select book_id,count(*) as current_borrowers from borrowing_records r
where return_date is null
group by book_id)
select l.book_id,title,author,genre,publication_year,current_borrowers from library_books l
inner join cte c on c.book_id=l.book_id and c.current_borrowers=l.total_copies
order by current_borrowers desc,title 