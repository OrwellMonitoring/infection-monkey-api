<!-- Generator: Widdershins v4.0.1 -->

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="fastapi-run">Run</h1>

## run_island_run__conf_name__get

<a id="opIdrun_island_run__conf_name__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /run/{conf_name} \
  -H 'Accept: application/json'

```

`GET /run/{conf_name}`

*Run Island*

<h3 id="run_island_run__conf_name__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|conf_name|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "message": "string"
}
```

<h3 id="run_island_run__conf_name__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ApiResponse](#schemaapiresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## kill_monkeys_kill_get

<a id="opIdkill_monkeys_kill_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /kill \
  -H 'Accept: application/json'

```

`GET /kill`

*Kill Monkeys*

> Example responses

> 200 Response

```json
{
  "code": 0,
  "message": "string"
}
```

<h3 id="kill_monkeys_kill_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ApiResponse](#schemaapiresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## reset_reset_get

<a id="opIdreset_reset_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /reset \
  -H 'Accept: application/json'

```

`GET /reset`

*Reset*

> Example responses

> 200 Response

```json
{
  "code": 0,
  "message": "string"
}
```

<h3 id="reset_reset_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ApiResponse](#schemaapiresponse)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-config">Config</h1>

## get_configs_configs_get

<a id="opIdget_configs_configs_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /configs \
  -H 'Accept: application/json'

```

`GET /configs`

*Get Configs*

> Example responses

> 200 Response

```json
{
  "configs": [
    "string"
  ]
}
```

<h3 id="get_configs_configs_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ConfList](#schemaconflist)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_ApiResponse">ApiResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiresponse"></a>
<a id="schema_ApiResponse"></a>
<a id="tocSapiresponse"></a>
<a id="tocsapiresponse"></a>

```json
{
  "code": 0,
  "message": "string"
}

```

ApiResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|true|none|none|
|message|string|true|none|none|

<h2 id="tocS_ConfList">ConfList</h2>
<!-- backwards compatibility -->
<a id="schemaconflist"></a>
<a id="schema_ConfList"></a>
<a id="tocSconflist"></a>
<a id="tocsconflist"></a>

```json
{
  "configs": [
    "string"
  ]
}

```

ConfList

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|configs|[string]|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[string]|true|none|none|
|msg|string|true|none|none|
|type|string|true|none|none|


