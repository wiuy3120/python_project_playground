SELECT
  A.date AS date,
  A.zone_id AS zone_id,
  A.ad_id AS ad_id,
  A.tags AS tags,
  A.creator AS creator,
  A.ad_name AS ad_name,
  A.campaign_name AS campaign_name,
  A.order_id AS order_id,
  A.order_name AS order_name,
  A.source_id AS source_id,
  A.category_id AS category_id,
  A.rate_unit_id AS rate_unit_id,
  A.ad_kind_id AS ad_kind_id,
  A.impressions AS impressions,
  A.clicks AS clicks,
  A.rev AS rev,
  A.rev_bid AS rev_bid,
  A.year AS year,
  A.yearweek AS yearweek,
  A.week AS week,
  A.year_week AS year_week,
  A.Zone__id AS Zone__id,
  A.Zone__noise_id AS Zone__noise_id,
  A.Zone__name AS Zone__name,
  A.Zone__kind AS Zone__kind,
  A.Zone__website_id AS Zone__website_id,
  A.Website__id AS Website__id,
  A.Website__name AS Website__name,
  A.Website__website_group_id AS Website__website_group_id,
  S.id AS Source__id,
  S.name AS Source__name,
  S.color AS Source__color,
  R.name AS Rate_unit_name
FROM
  (
    SELECT
      A.date AS date,
      A.zone_id AS zone_id,
      A.ad_id AS ad_id,
      A.tags AS tags,
      A.creator AS creator,
      A.ad_name AS ad_name,
      A.campaign_name AS campaign_name,
      A.order_id AS order_id,
      A.order_name AS order_name,
      A.source_id AS source_id,
      A.category_id AS category_id,
      A.rate_unit_id AS rate_unit_id,
      A.ad_kind_id AS ad_kind_id,
      A.impressions AS impressions,
      A.clicks AS clicks,
      A.rev AS rev,
      A.rev_bid AS rev_bid,
      A.year AS year,
      A.yearweek AS yearweek,
      A.week AS week,
      A.year_week AS year_week,
      Zone.id AS Zone__id,
      Zone.noise_id AS Zone__noise_id,
      Zone.name AS Zone__name,
      Zone.kind AS Zone__kind,
      Zone.website_id AS Zone__website_id,
      Website.id AS Website__id,
      Website.name AS Website__name,
      Website.website_group_id AS Website__website_group_id
    FROM
      (
        SELECT
          *,
          toYear(date) as year,
          toYearWeek(date, 7) as yearweek,
          (yearweek % 100) as week,
          toString(intDiv(yearweek, 100)) || '-' || leftPad(toString(week), 2, '0') AS year_week
        FROM
          adtima_product_data.metabase_migrating_table_3
      ) AS source
     
LEFT JOIN adtima_product_data.zone AS Zone ON A.zone_id = Zone.id
      LEFT JOIN adtima_product_data.website AS Website ON Zone.website_id = Website.id
  ) AS source
  LEFT JOIN adtima_product_data.source AS S ON A.source_id = S.id
  LEFT JOIN adtima_product_data.rate_unit AS R ON R.id = A.rate_unit_id
