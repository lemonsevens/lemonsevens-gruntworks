
- [Fibery API Docs](#fibery-api-docs)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Authentication](#authentication)
    - [Managing tokens](#managing-tokens)
    - [Request limits](#request-limits)
  - [Schema API](#schema-api)
    - [**Get Schema**](#get-schema)
  - [Type API](#type-api)
    - [Type and Field permissions](#type-and-field-permissions)
    - [Create Type](#create-type)
    - [Rename Type](#rename-type)
    - [**Delete Type**](#delete-type)
  - [Field API](#field-api)
    - [Create Field](#create-field)
    - [Rename Field](#rename-field)
    - [Delete Field](#delete-field)
    - [FAQ](#faq)
  - [Entity API](#entity-api)
    - [Overview](#overview)
    - [Select Fields](#select-fields)
    - [Select aggregates](#select-aggregates)
    - [Select rich text Field](#select-rich-text-field)
    - [Filter Entities](#filter-entities)
    - [Order Entities](#order-entities)
    - [Create Entity](#create-entity)
    - [Update Entity](#update-entity)
    - [Add comment](#add-comment)
    - [Delete Entity](#delete-entity)
  - [Views API](#views-api)
    - [Getting views](#getting-views)
    - [Creating views](#creating-views)
    - [Updating views](#updating-views)
    - [Deleting views](#deleting-views)
  - [API FAQ](#api-faq)
    - [How to create Single-Select and Multi-Select fields via Integration API?](#how-to-create-single-select-and-multi-select-fields-via-integration-api)
    - [How can I create a Muli Select using the API?](#how-can-i-create-a-muli-select-using-the-api)
    - [Is there a way to see logs and print out something in Script Actions (Execute Javascript Code)?](#is-there-a-way-to-see-logs-and-print-out-something-in-script-actions-execute-javascript-code)
    - [How to call the Location field via API?](#how-to-call-the-location-field-via-api)
    - [How to update the avatar with a URL to an image?](#how-to-update-the-avatar-with-a-url-to-an-image)
    - [How to update the Icon Field?](#how-to-update-the-icon-field)
    - [How to work with the Lookup Field?](#how-to-work-with-the-lookup-field)
    - [How to work with Documents?](#how-to-work-with-documents)
    - [API Token Activity Details](#api-token-activity-details)
    - [Troubleshooting](#troubleshooting)


# Fibery API Docs

## Introduction

The Fibery API provides a way to integrate Fibery with your external systems and automate routine tasks. 

Here is the list of things you can do:
* Understand you workspace schema via [[User Guide/Guide: Schema API#^dee06c51-f937-11ec-aafd-7332cdf16307/3af5c640-b136-11ee-80ca-873024c45f1c]] (use to understand what databases and fields you have).
* Customize Apps (Spaces) by creating, renaming and deleting Types (Databases) and Fields: [[User Guide/Guide: Type API#^dee06c51-f937-11ec-aafd-7332cdf16307/1f8e9660-b137-11ee-80ca-873024c45f1c]] and [[User Guide/Guide: Field API#^dee06c51-f937-11ec-aafd-7332cdf16307/39c0af60-b13b-11ee-80ca-873024c45f1c]]. 
* Read, create, update and delete Entities: [[User Guide/Guide: Entity API#^dee06c51-f937-11ec-aafd-7332cdf16307/5343d5a0-b13d-11ee-80ca-873024c45f1c]]. 
* Work with [rich text Fields](https://the.fibery.io/@public/User_Guide/Guide/Entity-API-264/anchor=Select-rich-text-Field--f9838a54-3d74-4f49-9f5d-9195731c7e89).
* Upload, attach and download files: [[User Guide/Guide: File API#^dee06c51-f937-11ec-aafd-7332cdf16307/ce14f0d0-b146-11ee-80ca-873024c45f1c]]. 
* Update other tools when something changes in Fibery using [[User Guide/Guide: Webhooks#^dee06c51-f937-11ec-aafd-7332cdf16307/97b96b60-b12d-11ee-8934-b50d61a093b6]].
* Automate routine actions with programmable action buttons and rules: [[User Guide/Guide: Scripts in Automations#^dee06c51-f937-11ec-aafd-7332cdf16307/a9dfb6e0-fa19-11ec-a00c-9384c37c027a]]. 
* Integrate your custom data into Fibery database using custom apps.

If something is missing, please describe your use case in [the community](https://community.fibery.io/ "https://community.fibery.io/") — we’ll try our best to help.

> [//]: # (callout;icon-type=emoji;icon=:bulb:;color=#fba32f)
> Fibery also has [[User Guide/Guide: GraphQL API#^dee06c51-f937-11ec-aafd-7332cdf16307/3c325c60-b11f-11ee-8934-b50d61a093b6]], so you may check it. 

> [//]: # (callout;icon-type=emoji;icon=:point_up:;color=#1fbed3)
> In the interface, Type = Database, App = Space. To find out why, check [Terminology](https://the.fibery.io/User_Guide/Guide/Fibery-API-Overview-279/anchor=Terminology--15f750ec-571c-48f6-9b0b-6861222c1a27).

## Getting Started

Fibery API is based on commands. Both reading and editing data means sending a POST request with JSON payload to `https://YOUR_ACCOUNT.fibery.io/api/commands` endpoint.

The endpoint works with batches of commands. The request should contain an array of commands with their names and arguments. You'll get an array back too. Take a look at the example below in which we retrieve the basic info about a user.

While there are no official clients for any platform, there is an [unofficial API client for Node.js](https://gitlab.com/fibery-community/unofficial-js-client). 

[https://gitlab.com/fibery-community/unofficial-js-client](https://gitlab.com/fibery-community/unofficial-js-client)

It mostly follows the API functionality, but makes it easier to create a domain Type, a relation or a single-select Field.

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const users = await fibery.entity.query({
    "q/from": "fibery/user",
    "q/select": ["fibery/id","user/name"],
    "q/limit": 1
});
```

Here’s the result:

```
[
  {
    "fibery/id": "7dcf4730-82d2-11e9-8a28-82a9c787ee9d",
    "user/name": "Arthur Dent"
  }
]
```

And here are cURL examples:

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
  -H 'Authorization: Token YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '[
    {
      "command": "fibery.entity/query",
      "args": {
        "query": {
          "q/from": "fibery/user",
          "q/select": ["fibery/id", "user/name"],
          "q/limit": 1
        }
      }
    }
  ]'
```

Here’s the result:

```
[
  {
    "success": true,
    "result": [
      {
        "fibery/id": "7dcf4730-82d2-11e9-8a28-82a9c787ee9d",
        "user/name": "Arthur Dent"
      }
    ]
  }
]
```

## Authentication

Fibery API uses token-based authentication. That means you need to pass your API token with every request. This token should be the same for all requests, there is no need to generate a new one each time. Your API token carries the same privileges as your user, so be sure to keep it secret.

```
# To authenticate set the Authorization header in this way:

curl -X POST "https://YOUR_ACCOUNT.fibery.io/api/commands" \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     ...
     
# JavaScript     

const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});
```

Make sure to replace your account name and token with the actual values

### Managing tokens

The number of tokens is limited to **3 per user**.

You can generate, list and delete tokens on the "API Tokens" page available from the workspace menu.

![image.png](https://the.fibery.io/api/files/d3b48652-27a9-4b94-b3d5-e14ad723027d#width=883&height=589 "")

You can also manage the tokens directly using the API. The following endpoints are available to manage access tokens:
* `GET /api/tokens` — lists all access tokens that were given to current user
* `POST /api/tokens` — creates new token for current user
* `DELETE /api/tokens/:token_id` — deletes token by id

> [//]: # (callout;icon-type=emoji;icon=:woman-shrugging:;color=#fc551f)
> You need to be authenticated with a browser cookie or with an already existing token when accessing these endpoints.

### Request limits

To ensure system stability and consistent user experience, our API is rate-limited.

Rate-limited requests will return a "Too Many Requests" error (HTTP response status `429`). The rate limit for incoming requests is **3 requests per second per token**.

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#fba32f)
> Rate limits may change. In the future we may adjust rate limits to balance for demand and reliability.

## Schema API

Fibery Schema is the metadata describing Types (Databases) and their Fields. Basically, it's everything you see on the `Workspace Map` screen and a few auxiliary Types (Databases):

![Screenshot 2024-01-12 at 12.36.30 PM.png](https://the.fibery.io/api/files/603698fb-bb77-47c4-b7fa-b651a9c23af0#width=2590&height=1520 "")

### **Get Schema**

Get all Types (Databases), Fields and their metadata.

> [//]: # (callout;icon-type=emoji;icon=:point_up:;color=#1fbed3)
> In Fibery UI Type = Database, App=Space. To find out why, check [Terminology](https://the.fibery.io/User_Guide/Guide/Fibery-API-Overview-279/anchor=Terminology--15f750ec-571c-48f6-9b0b-6861222c1a27 "https://the.fibery.io/User_Guide/Guide/Fibery-API-Overview-279/anchor=Terminology--15f750ec-571c-48f6-9b0b-6861222c1a27").

Take a look at the [Type](https://the.fibery.io/User_Guide/Guide/Type-API-262) and [Field](https://the.fibery.io/User_Guide/Guide/Field-API-263) sections for the metadata description.

Fibery Schema for a median account takes a few hundred kilobytes.

#### Command parameters

| Parameter (required in bold) | Default | Description                                      | Example |
| ---------------------------- | ------- | ------------------------------------------------ | ------- |
| `with-description?`          | false   | Whether to include type descriptions in response | true    |

```
# JavaScript

const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});
const schema = await fibery.getSchema();

# cURL

curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
  -H 'Authorization: Token YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '[{ "command": "fibery.schema/query" }]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": {
      "fibery/id": "fd5d9550-3779-11e9-9162-04d77e8d50cb",
      "fibery/types": [
        {
          "fibery/name": "software-development/user-story",
          "fibery/fields": [
            {
              "fibery/name": "fibery/modification-date",
              "fibery/type": "fibery/date-time",
              "fibery/meta": {
                "fibery/modification-date?": true,
                "fibery/readonly?": true,
                "fibery/default-value": "$now",
                "fibery/secured?": false,
                "fibery/required?": true,
                "ui/object-editor-order": 8
              },
              "fibery/id": "e36a91b1-3f4b-11e9-8051-8fb5f642f8a5"
            },
            {
              "fibery/name": "assignments/assignees",
              "fibery/type": "fibery/user",
              "fibery/meta": {
                "fibery/collection?": true,
                "ui/object-editor-order": 4,
                "fibery/relation": "c3e75ca4-8d15-11e9-b98a-9abbdf4720ab"
              },
              "fibery/id": "2cd92374-3839-11e9-9162-04d77e8d50cb"
            }
            #...other Fields
          ],
          "fibery/meta": {
            "fibery/primitive?": false,
            "fibery/domain?": true,
            "ui/color": "#068cba",
            "app/mixins": {
              "fibery/rank-mixin": true,
              "assignments/assignments-mixin": true,
              "Files/Files-mixin": true,
              "workflow/workflow": true,
              "comments/comments-mixin": true
            },
            "fibery/secured?": true
          },
          "fibery/id": "2c4213ae-3839-11e9-9162-04d77e8d50cb"
        }
        #...other Types
      ],
      "fibery/meta": {
        "fibery/version": "1.0.62",
        "fibery/rel-version": "1.0.6",
        "fibery/maintenance?": false,
        "maintenance?": false
      }
    }
  }
]
```

## Type API

Type is a template for Entities of some kind: Bugs, Teams, Objectives, etc. 

> [//]: # (callout;icon-type=emoji;icon=:point_up:;color=#1fbed3)
> In the interface, Type = Database, App = Space. To find out why, check [Terminology](https://the.fibery.io/User_Guide/Guide/Fibery-API-Overview-279/anchor=Terminology--15f750ec-571c-48f6-9b0b-6861222c1a27).

It consists of metadata and Fields.

![2024-01-12 12.43.42.gif](https://the.fibery.io/api/files/ad0d48f5-b2ea-43c7-a466-1d9b38f2de9d#align=%3Aalignment%2Fblock-left&width=408&height=483 "")

### Type and Field permissions

Imagine you've got a Type `Task` with a Field called `Effort`. Here's how permissions apply depending on `secured?` parameter:

|                       |                                   |
| --------------------- | --------------------------------- |
|                       | **Task `secured?`**               |
| ❌                     | ✅                                 |
| **Effort `secured?`** | ❌                                 | Everyone has access to all fields                                                               | Everyone has access to Effort, but not to other `secured?` fields |
| ✅                     | Everyone has access to all fields | Everyone has access to Task’s non-secured Fields like Id, but permissions are applied to Effort |

### Create Type

Every Type is a part of some Space. If Type's Space does not exist yet, create or install the Space.

To create a fully functional Type, we'll execute two commands:

1. `schema.type/create` to create a Type with at least five mandatory primitive Fields:
   * `fibery/id`
   * `fibery/public-id`
   * `fibery/creation-date`
   * `fibery/modification-date`
   * `${space}/name`
2. `fibery.app/install-mixins` to be able to prioritize Type's Entities.

For auxiliary Types, that are hidden from `Workspace Map` screen, `${space}/name` Field and `rank` Mixin are optional. Just skip these parts when creating a Type.

Auxiliary Types might be useful as an Entity-based storage — that's how our User's favourite pages and recent items work, for example.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

// 5 primitive fields are created and rank Mixin is installed automatically for domain Types
await fibery.type.createBatch([
  {
    'fibery/name': 'Cricket/Player',
    'fibery/meta': {
      'fibery/domain?': true,
      'fibery/secured?': true,
      'ui/color': '#F7D130'
    },
    'fibery/fields': [
      {
        "fibery/name": 'user/salary',
        "fibery/type": 'fibery/int',
        "fibery/meta": {
          "fibery/secured?": true
        }
      }
    ]
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
        {
          "command": "fibery.schema/batch",
          "args": {
            "commands": [
              {
                "command": "schema.type/create",
                "args": {
                  "fibery/name": "Cricket/Player",
                  "fibery/meta": {
                    "fibery/domain?": true,
                    "fibery/secured?": true,
                    "ui/color": "#F7D130"
                  },
                  "fibery/fields": [
                    {
                      "fibery/name": "Cricket/name",
                      "fibery/type": "fibery/text",
                      "fibery/meta": {
                        "fibery/secured?": false,
                        "ui/title?": true
                      }
                    },
                    {
                      "fibery/name": "fibery/id",
                      "fibery/type": "fibery/uuid",
                      "fibery/meta": {
                        "fibery/secured?": false,
                        "fibery/id?": true,
                        "fibery/readonly?": true
                      }
                    },
                    {
                      "fibery/name": "fibery/public-id",
                      "fibery/type": "fibery/text",
                      "fibery/meta": {
                        "fibery/secured?": false,
                        "fibery/public-id?": true,
                        "fibery/readonly?": true
                      }
                    },
                    {
                      "fibery/name": "fibery/creation-date",
                      "fibery/type": "fibery/date-time",
                      "fibery/meta": {
                        "fibery/secured?": false,
                        "fibery/creation-date?": true,
                        "fibery/readonly?": true,
                        "fibery/default-value": "$now"
                      }
                    },
                    {
                      "fibery/name": "fibery/modification-date",
                      "fibery/type": "fibery/date-time",
                      "fibery/meta": {
                        "fibery/modification-date?": true,
                        "fibery/required?": true,
                        "fibery/readonly?": true,
                        "fibery/default-value": "$now",
                        "fibery/secured?": false
                      }
                    },
                    {
                      "fibery/name": "user/salary",
                      "fibery/type": "fibery/int",
                      "fibery/meta": {
                        "fibery/secured?": true
                      }
                    }
                  ]
                }
              },
              {
                "command": "fibery.app/install-mixins",
                "args": {
                  "types": {
                    "Cricket/Player": [
                      "fibery/rank-mixin"
                    ]
                  }
                }
              }
            ]
          }
        }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

#### Command parameters

| Parameter (required in bold) | Default        | Description                                                                                             | Example            |
| ---------------------------- | -------------- | ------------------------------------------------------------------------------------------------------- | ------------------ |
| **`fibery/name`**            |                | Type name in `${space}/${name}` format                                                                  | `CRM/Lead`         |
| `fibery/id`                  | Auto-generated | UUID                                                                                                    | `fd5d9550-3779...` |
| meta.`fibery/domain?`        | false          | Domain Types are available as cards on Views                                                            | true               |
| meta.**`fibery/secured?`**   |                | [Permissions](https://api.fibery.io/?javascript#type-and-field-permissions) apply to secured Types only | true               |
| meta.`ui/color?`             | #000000        | HEX color to use in Entity badges                                                                       | #F7D130            |
| meta.**`fibery/fields`**     |                | Array of [Fields](https://api.fibery.io/?javascript#field) including 5 primitive ones above             |                    |

### Rename Type

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.type.renameBatch([
  {
    'from-name': 'Cricket/Referee',
    'to-name': 'Cricket/Umpire'
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.type/rename",
                 "args": {
                   "from-name": "Cricket/Referee",
                   "to-name": "Cricket/Umpire"
                 }
               }
             ]
           }
         }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

#### **Command parameters**

| Parameter (required in bold) | Description                                    | Example           |
| ---------------------------- | ---------------------------------------------- | ----------------- |
| **`from-name`**              | Current Type name in `${space}/${name}` format | `Cricket/Referee` |
| **`to-name`**                | New Type name in `${space}/${name}` format     | `Cricket/Umpire`  |

### **Delete Type**

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.type.deleteBatch([
  {
    'name': 'Cricket/Umpire',
    'delete-entities?': true,
    'delete-related-fields?': true
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.type/delete",
                 "args": {
                   "name": "Cricket/Umpire",
                   "delete-entities?": true,
                   "delete-related-fields?": true
                 }
               }
             ]
           }
         }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

#### Command parameters

| Parameter (required in bold) | Default | Description                                                                                                        | Example          |
| ---------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **`name`**                   |         | Type name in `${space}/${name}` format                                                                             | `Cricket/Umpire` |
| `delete-entities?`           | false   | Delete all Entities of this Type? See the behavior in the table below.                                             | true             |
| `delete-related-fields?`     | false   | Delete all related Fields like `Criket/Favourite Umpire` in `Cricket/Player`? See the behavior in the table below. | true             |

#### `delete?` parameter behavior

|                                  |                         |
| -------------------------------- | ----------------------- |
|                                  | **`delete?` parameter** |
| **false**                        | **true**                |
| **Entities (or related Fields)** | **don't exist**         | Type is deleted                                   | Type is deleted |
| **exist**                        | Error is thrown         | Type and Entities (or related Fields) are deleted |

Related single-select `enum` Types are not deleted even with `delete-related-fields?` enabled. Delete these Types separately the same way you delete the original Type.


## Field API

Field is a part of Type (Database). Learn more about [[User Guide/Guide: Fields#^dee06c51-f937-11ec-aafd-7332cdf16307/fddf0f40-f940-11ec-83f8-c3aae135ffa6]] in the guide.

> [//]: # (callout;icon-type=emoji;icon=:point_up:;color=#1fbed3)
> In the interface, Type = Database, App = Space. To find out why, check [Terminology](https://the.fibery.io/@public/User_Guide/Guide/Fibery-API-Overview-279/anchor=Terminology--15f750ec-571c-48f6-9b0b-6861222c1a27).

### Create Field

#### Primitive Field

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.field.createBatch([
  {
    'fibery/holder-type': 'Cricket/Player',
    'fibery/name': 'Cricket/Salary',
    'fibery/type': 'fibery/int',
    'fibery/meta': {
        'fibery/readonly?': false,
        'fibery/default-value': 1000,
        'ui/number-unit': 'USD'
    }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.field/create",
                 "args": {
                   "fibery/holder-type": "Cricket/Player",
                   "fibery/name": "Cricket/Salary",
                   "fibery/type": "fibery/int",
                   "fibery/meta": {
                       "fibery/readonly?": false,
                       "fibery/default-value": 1000,
                       "ui/number-unit": "USD"
                   }
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

Primitive Field types

| Field type         | Example                                                 | Comments                                                                                       |
| ------------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `fibery/int`       | 42                                                      |                                                                                                |
| `fibery/decimal`   | 0.33                                                    |                                                                                                |
| `fibery/bool`      | true                                                    |                                                                                                |
| `fibery/text`      | Don't panic                                             | Up to 1k characters. Can be styled using `ui/type` meta flag:  text \| email \| phone \| url   |
| `~~fibery/email~~` | [~~contact@megadodo.com~~](mailto:contact@megadodo.com) | This field type is deprecated. Use a "fibery/text" field with `ui/type` meta set to "email": { |
  "ui/type": "email"
} |
| `fibery/emoji` | 🏏 |  |
| `fibery/date` | 1979-10-12 |  |
| `fibery/date-time` | 2019-06-24T12:25:20.812Z |  |
| `fibery/date-range` | {
  "start": "2019-06-27",
  "end": "2019-06-30"
} |  |
| `fibery/date-time-range` | {
  "start": "2019-06-18T02:40:00.000Z",
  "end": "2019-07-25T11:40:00.000Z"
} |  |
| `fibery/location` | {
  "longitude": 2.349606,
  "latitude": 48.890764,
  "fullAddress": "Métro Marcadet Poissonniers, 67 boulevard Barbès, Paris, 75018, France",
  "addressParts": {
    "city": "Paris",
    "country": "France"
  }
} | All address parts are optional. Check supported values in [[User Guide/Guide: Location field#^dee06c51-f937-11ec-aafd-7332cdf16307/3aed8d10-b347-11ed-bb10-bb6ccb6277a9]]  |
| `fibery/uuid` | acb5ef80-9679-11e9-bc42-526af7764f64 |  |
| `fibery/rank` | 1000 |  |
| `fibery/json-value` |  { "paranoid?": true } |  |

Command parameters

| Parameter (required in bold) | Description                                                              | Example          |
| ---------------------------- | ------------------------------------------------------------------------ | ---------------- |
| **`fibery/holder-type`**     | Holder Type name in `${space}/${name}` format                            | `Cricket/Player` |
| **`fibery/name`**            | Field name in `${space}/${name}` format.                                 | `Cricket/Salary` |
| **`fibery/type`**            | One of the primitive Field types above or a Type for a one-way relation. | `fibery/int`     |
| meta.`fibery/readonly?`      | If users are able to change value from UI                                | true             |
| meta.`fibery/default-value`  | The value automatically set when a new entity is created                 | "(empty)"        |

#### Relation (entity \[collection\] Field)

To create a relation between two Types, we create a pair of entity \[collection\] Fields and connect them with a unique identifier.

The relation is to-one by default. Set entity Field's meta.`fibery/collection?` to `true` for to-many relation.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

// The unofficial client is closer to UI than to API here.
// Note the  missing 'fibery/' namespace in Field type name and meta parameter —
// these things are unique to the client.
await fibery.field.createBatch([
  {
    'fibery/holder-type': 'Cricket/Player',
    'fibery/name': 'Cricket/Current Team',
    'fibery/type': 'relation',
    meta: {
      to: 'Cricket/Team',
      toName: 'Cricket/Current Roster',
      isFromMany: true,
      isToMany: false
    }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.field/create",
                 "args": {
                   "fibery/holder-type": "Cricket/Player",
                   "fibery/name": "Cricket/Current Team",
                   "fibery/type": "Cricket/Team",
                   "fibery/meta": {
                     "fibery/relation": "d9e9ec34-9685-11e9-8550-526af7764f64"
                   }
                 }
               },
               {
                 "command": "schema.field/create",
                 "args": {
                   "fibery/holder-type": "Cricket/Team",
                   "fibery/name": "Cricket/Current Roster",
                   "fibery/type": "Cricket/Player",
                   "fibery/meta": {
                     "fibery/collection?": true,
                     "fibery/relation": "d9e9ec34-9685-11e9-8550-526af7764f64"
                   }
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

Command parameters

| Parameter (required in bold) | Description                                           | Example                |
| ---------------------------- | ----------------------------------------------------- | ---------------------- |
| **`fibery/holder-type`**     | Holder Type name in `${space}/${name}` format         | `Cricket/Player`       |
| **`fibery/name`**            | Field name in `${space}/${name}` format.              | `Cricket/Current Team` |
| **`fibery/type`**            | Related Type name in `${space}/${name}` format        | `Cricket/Team`         |
| meta.**`fibery/relation`**   | UUID shared between the pair of Fields.               | d9e9ec34-96...         |
| meta.`fibery/collection?`    | `true` for to-many relation (entity collection Field) | true                   |
| meta.`fibery/readonly?`      | If users are able to change value from UI             | true                   |

#### Single-select Field

A single-select Field is not what it seems to be. Actually, every single-select option is an Entity of a newly created special Type.

This way unlocks 'name on UI + value in Formula' scenario (think `Self conviction` → `0.01` in GIST) and enables an easy transition to a fully functional Type.

To create a single-select Field we should:

1. Create a new `enum` Type
2. Create a Field of the newly created `enum` Type
3. Create an Entity for each single-select option
4. Make the selection required and set the default value

The new `enum` Type name is built using this format: `${space}/${field}_${app}/${holder-type}`.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

// The unofficial client is closer to UI than to API here.
// Note the missing 'fibery/' namespace in Field type name and meta parameter —
// these things are unique to the client.
await fibery.field.createBatch([
  {
    'fibery/holder-type': 'Cricket/Player',
    'fibery/name': 'Cricket/Batting Hand',
    'fibery/type': 'single-select',
    meta: {
      options: [
        { name: 'Right' },
        { name: 'Left' }
      ]
    }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.command/batch",
           "args": {
             "commands": [
               {
                 "command": "fibery.schema/batch",
                 "args": {
                   "commands": [
                     {
                       "command": "schema.enum/create",
                       "args": {
                         "fibery/name": "Cricket/Batting Hand_Cricket/Player"
                       }
                     },
                     {
                       "command": "schema.field/create",
                       "args": {
                         "fibery/holder-type": "Cricket/Player",
                         "fibery/name": "Cricket/Batting Hand",
                         "fibery/type": "Cricket/Batting Hand_Cricket/Player"
                       }
                     }
                   ]
                 }
               },
               {
                 "command": "fibery.entity/create",
                 "args": {
                   "type": "Cricket/Batting Hand_Cricket/Player",
                   "entity": {
                     "enum/name": "Right",
                     "fibery/id": "4a3ffb10-9747-11e9-9def-016e5ea5e162",
                     "fibery/rank": 0
                   }
                 }
               },
               {
                 "command": "fibery.entity/create",
                 "args": {
                   "type": "Cricket/Batting Hand_Cricket/Player",
                   "entity": {
                     "enum/name": "Left",
                     "fibery/id": "4a402220-9747-11e9-9def-016e5ea5e162",
                     "fibery/rank": 1000000
                   }
                 }
               },
               {
                 "command": "fibery.schema/batch",
                 "args": {
                   "commands": [
                     {
                       "command": "schema.field/set-meta",
                       "args": {
                         "name": "Cricket/Batting Hand",
                         "holder-type": "Cricket/Player",
                         "key": "fibery/default-value",
                         "value": {
                           "fibery/id": "4a3ffb10-9747-11e9-9def-016e5ea5e162"
                         }
                       }
                     },
                     {
                       "command": "schema.field/set-meta",
                       "args": {
                         "name": "Cricket/Batting Hand",
                         "holder-type": "Cricket/Player",
                         "key": "fibery/required?",
                         "value": true
                       }
                     }
                   ]
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "success": true,
        "result": "ok"
      },
      {
        "success": true,
        "result": {
          "fibery/id": "4a3ffb10-9747-11e9-9def-016e5ea5e162",
          "fibery/public-id": "1",
          "enum/name": "Right",
          "fibery/rank": 0
        }
      },
      {
        "success": true,
        "result": {
          "fibery/id": "4a402220-9747-11e9-9def-016e5ea5e162",
          "fibery/public-id": "2",
          "enum/name": "Left",
          "fibery/rank": 1000000
        }
      },
      {
        "success": true,
        "result": "ok"
      }
    ]
  }
]
```

#### Rich text Field

In Fibery, every [[User Guide/Guide: Rich Text#^dee06c51-f937-11ec-aafd-7332cdf16307/bc363890-fa15-11ec-a00c-9384c37c027a]] Field instance is, in fact, a collaborative document.

It means that for each Entity with N rich text Fields Fibery automatically creates N documents. Each of these documents is stored in Document Storage and is connected to its Entity through an auxiliary `Collaboration~Documents/Document` Entity:

Entity --- (magic) ---> `Collab Doc/Document` --- (`fibery/secret`) ---> Document in Storage

So to create a rich text Field we just connect our Type with `Collaboration~Documents/Document` Type. Type `Collaboration~Documents/Document` has a special property, namely, the entities of this Type inherit access from their Parent Entity. To indicate that Parent-Child relationship we pass `fibery/entity-component?` meta flag, but only for ordinary Fields (e.g. not Lookup and not Formula)

Selecting and updating a rich text Field is a two-step process:

1. Get `fibery/secret` of the related Document.
2. Work with this Document via `api/documents` Storage endpoint.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

// The unofficial client is closer to UI than to API here.
// Note the missing 'fibery/' namespace in Field type name and meta parameter —
// these things are unique to the client.
await fibery.field.createBatch([
  {
    'fibery/holder-type': 'Cricket/Player',
    'fibery/name': 'Cricket/Bio',
    'fibery/type': 'Collaboration~Documents/Document',
    'fibery/meta': {
      'fibery/entity-component?': true,
    }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.field/create",
                 "args": {
                   "fibery/holder-type": "Cricket/Player",
                   "fibery/name": "Cricket/Bio",
                   "fibery/type": "Collaboration~Documents/Document",
                   "fibery/meta": {
                     "fibery/entity-component?": true,
                   },
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

### Rename Field

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#d40915)
> At the moment, renaming a Field breaks related Views, Formulas and Reports. After you rename a Field, make sure to update the related configs.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.field.renameBatch([
  {
    'holder-type': 'Cricket/Player',
    'from-name': 'Cricket/Position',
    'to-name': 'Cricket/Role'
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.field/rename",
                 "args": {
                   "holder-type": "Cricket/Player",
                   "from-name": "Cricket/Position",
                   "to-name": "Cricket/Role"
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
    {
        "success": true,
        "result": "ok"
    }
]
```

Command parameters

| Parameter (required in bold) | Description                                     | Example            |
| ---------------------------- | ----------------------------------------------- | ------------------ |
| **`holder-type`**            | Holder Type name in `${space}/${name}` format   | `Cricket/Player`   |
| **`from-name`**              | Current Field name in `${space}/${name}` format | `Cricket/Position` |
| **`to-name`**                | New Field name in `${space}/${name}` format     | `Cricket/Role`     |

### Delete Field

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.field.deleteBatch([
  {
    'holder-type': 'Cricket/Player',
    'name': 'Cricket/Role',
    'delete-values?': true
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.schema/batch",
           "args": {
             "commands": [
               {
                 "command": "schema.field/delete",
                 "args": {
                   "holder-type": "Cricket/Player",
                   "name": "Cricket/Role",
                   "delete-values?": true
                 }
               }
             ]
           }
         }
       ]'
```

Result (cURL):

```
[
    {
        "success": true,
        "result": "ok"
    }
]
```

#### **Command parameters**

| Parameter (required in bold) | Default | Description                                   | Example          |
| ---------------------------- | ------- | --------------------------------------------- | ---------------- |
| **`holder-type`**            |         | Holder Type name in `${space}/${name}` format | `Cricket/Player` |
| **`name`**                   |         | Field name in `${space}/${name}` format       | `Cricket/Role`   |
| **`delete-values?`**         | false   | See the behavior in the table below           | true             |

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#1fbed3)
> To remove a relation, delete both entity \[collection\] Fields within the same `fibery.schema/batch` command.

`delete-values?` parameter behavior

|                                           |                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------- |
|                                           | **`delete-values?`**                                                |
| **false**                                 | **true**                                                            |
| **Field type**                            | **Empty [primitive](https://api.fibery.io/#primitive-field) Field** | Field is deleted                                       | Field is deleted |
| **Non-empty primitive Field**             | Error is thrown                                                     | Field and values are deleted                           |
| **Empty entity \[collection\] Field**     | Field is deleted                                                    | Field is deleted                                       |
| **Non-empty entity \[collection\] Field** | Error is thrown                                                     | Field and links (but not related Entities) are deleted |

### FAQ

##### Is there a way to modify the `meta.fibery readonly?` value? Is there any way to convert a field away from read-only?

Use `"command": "schema.field/set-meta".`So, if you can set `meta readonly?` value to false, that has to work.

##### How to create header anchor links in a script?

If you retrieve the doc content as JSON (instead of markdown) you will find that paragraphs have attributes, including the ‘level’ and a GUID.\
The level will tell you if it’s a header. and anchors are formed by adding the GUID property to the base URL.


## Entity API

### Overview

The general shape of an entity query is:

```
{
  "q/from": <database name> // "fibery/user", "Kanban/Story"
  "q/select": <select>
  "q/where": <where>
  "q/offset": <integer>
  "q/order-by": <order-by>
  "q/limit": <integer> | "q/no-limit"
}
```

The clauses are directly analogous to SQL's from, select, where, offset, order by and limit.

q/from, q/select and q/limit are required.

This section describes a comprehensive example. See the sections below for a more detailed explanation:
* select Fields
* filter Entities
* order Entities

Get info about cricket players born since 1986 ordered by height and age:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
  'q/from': 'Cricket/Player',
  'q/select': [
      'fibery/id',
      'fibery/public-id',
      'Cricket/name',
      'Cricket/Full Name',
      'Cricket/Born',
      'Cricket/Shirt Number',
      'Cricket/Height',
      'Cricket/Retired?',

      { 'Cricket/Batting Hand': ['enum/name'] },
      { 'Cricket/Current Team': ['Cricket/name'] },
      { 'user/Former Teams': { 'q/select': ['Cricket/name'], 'q/limit': 'q/no-limit' } },
      { '# of former teams': [ 'q/count', ['user/Former Teams', 'fibery/id'] ] }
  ],
  'q/where': ['>=', ['Cricket/Born'], '$birthday' ],
  'q/order-by': [
      [['Cricket/Height'], 'q/desc'],
      [['Cricket/Born'], 'q/asc']
  ],
  'q/limit': 3
}, { '$birthday': '1986-01-01' });
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": [
                  "fibery/id",
                  "fibery/public-id",
                  "Cricket/name",
                  "Cricket/Full Name",
                  "Cricket/Born",
                  "Cricket/Shirt Number",
                  "Cricket/Height",
                  "Cricket/Retired?",

                  { "Cricket/Batting Hand": ["enum/name"] },
                  { "Cricket/Current Team": ["Cricket/name"] },
                  { "user/Former Teams": { "q/select": ["Cricket/name"], "q/limit": "q/no-limit" } },
                  { "# of former teams": [ "q/count", ["user/Former Teams", "fibery/id"] ] }
                ],
               "q/where": [">=", ["Cricket/Born"], "$birthday" ],
               "q/order-by": [
                 [["Cricket/Height"], "q/desc"],
                 [["Cricket/Born"], "q/asc"]
               ],
               "q/limit": 3
             },
             "params": {
              "$birthday": "1986-01-01"
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "# of former teams": 6,
        "Cricket/Height": "1.79",
        "user/Former Teams": [
          { "Cricket/name": "Royal Challengers Bangalore" },
          { "Cricket/name": "Yorkshire" },
          { "Cricket/name": "Kolkata Knight Riders" },
          { "Cricket/name": "Kings XI Punjab" },
          { "Cricket/name": "Derbyshire" },
          { "Cricket/name": "Nottinghamshire" }
        ],
        "Cricket/Born": "1988-01-25",
        "fibery/id": "21e578b0-9752-11e9-81b9-4363f716f666",
        "Cricket/Shirt Number": 15,
        "Cricket/Full Name": "Cheteshwar Arvind Pujara",
        "fibery/public-id": "3",
        "Cricket/Retired?": false,
        "Cricket/Current Team": {
          "Cricket/name": "Saurashtra"
        },
        "Cricket/Batting Hand": {
          "enum/name": "Right"
        },
        "Cricket/name": "Cheteshwar Pujara"
      },
      {
        "# of former teams": 1,
        "Cricket/Height": "1.75",
        "user/Former Teams": [
          { "Cricket/name": "Delhi" }
        ],
        "Cricket/Born": "1988-11-05",
        "fibery/id": "20f9b920-9752-11e9-81b9-4363f716f666",
        "Cricket/Shirt Number": 18,
        "Cricket/Full Name": "Virat 'Chikoo' Kohli",
        "fibery/public-id": "1",
        "Cricket/Retired?": false,
        "Cricket/Current Team": {
          "Cricket/name": "Delhi"
        },
        "Cricket/Batting Hand": {
          "enum/name": "Right"
        },
        "Cricket/name": "Virat Kohli"
      },
      {
        "# of former teams": 4,
        "Cricket/Height": "1.75",
        "user/Former Teams": [
          { "Cricket/name": "Northern Districts" },
          { "Cricket/name": "Gloucestershire" },
          { "Cricket/name": "Yorkshire" },
          { "Cricket/name": "Barbados Tridents" }
        ],
        "Cricket/Born": "1990-08-08",
        "fibery/id": "216c2a00-9752-11e9-81b9-4363f716f666",
        "Cricket/Shirt Number": 22,
        "Cricket/Full Name": "Kane Stuart Williamson",
        "fibery/public-id": "2",
        "Cricket/Retired?": false,
        "Cricket/Current Team": {
          "Cricket/name": "Sunrisers Hyderabad"
        },
        "Cricket/Batting Hand": {
          "enum/name": "Right"
        },
        "Cricket/name": "Kane Williamson"
      }
    ]
  }
]
```

Command parameters

| Parameter (required in bold) | Description                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| query.**`q/from`**           | Database name in format `space/name`, such as Cricket/Player or fibery/user. Note that the case matters.                                  |
| query.**`q/select`**         | Array of primitive Fields, entity Field objects, objects with entity collection Fields subqueries and entity collection Field aggregates. |
| query.`q/where`              | Filter expression represented as an array.                                                                                                |
| query.`q/order-by`           | Array of sorting expressions — sorting by multiple Fields is supported.                                                                   |
| query.**`q/limit`**          | How many Entities to get. Pass `q/no-limit` to get all entities. In entity collection Fields subqueries only `q/no-limit` is supported .  |
| query.`q/offset`             | How many Entities to skip — useful for pagination.                                                                                        |
| `params`                     | Object of parameters for filter expressions in `{ "$param": value }` format.                                                              |

`Cricket/Player` Type used as an example

| Field name             | Field type              |
| ---------------------- | ----------------------- |
| `fibery/id`            | `fibery/uuid`           |
| `fibery/public-id`     | `fibery/text`           |
| `Cricket/name`         | `fibery/text`           |
| `Cricket/Full Name`    | `fibery/text`           |
| `Cricket/Born`         | `fibery/date`           |
| `Cricket/Shirt Number` | `fibery/int`            |
| `Cricket/Height`       | `fibery/decimal`        |
| `Cricket/Retired?`     | `fibery/bool`           |
| `Cricket/Batting Hand` | single-select           |
| `Cricket/Current Team` | entity Field            |
| `user/Former Teams`    | entity collection Field |

### Select Fields

In this example we demonstrate the select form known as "vector select". It's general form is:

```
<vec-select> = [ <field-name> | <vec-dereference> | <vec-subselect> ]
```

`<field-name>` is used for primitive fields (strings, numbers, booleans and the like). For example, to select id and name (both are text fields):

```
q/select: ["fibery/id", "fibery/name"]
```

`<field-name>` won't work for fields that point to other entities, because it's not clear what to include as the value. So the query must specify which fields from the referenced entity to include, and that's what the `<vec-dereference>` form does. Here, to add the id of the user in created-by, we add the `{thisField: [targetFields]` selector:

```
q/select: [
  "fibery/id",
  "fibery/name",
  {"fibery/created-by": ["fibery/id"]}
]
```

In the example above, `fibery/created-by` points to at most *one* user. When we have a field that point to *many* entities, that is a collection field, we should have a way to filter them. The dereference form is not sufficient and the `<vec-subselect>` form must be used. The subselect expression is a full query of its own (a subquery). Here we add to each result also a collection of assignees, where for each assignee we select only one field, id:

```
q/select: [
  "fibery/id",
  "fibery/name",
  {"fibery/created-by": ["fibery/id"]},
  {"user/assignees": {
    "q/select": ["fibery/id"],
    "q/limit": "q/no-limit"
   }}
]
```

Note that in some cases empty collections are returned as nulls.

In the example below we query entities from the `Cricket/Player` database and select:
* a primitive Field `Cricket/Full Name` of primitive type `fibery/text`
* a single-select `Cricket/Batting Hand`
* a related entity `Cricket/Current Team`
* an entity collection Field `user/Former Teams`
* an aggregate (the oldest former team year of foundation).

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
  'q/from': 'Cricket/Player',
  'q/select': [
    'Cricket/Full Name',

    { 'Cricket/Batting Hand': [
        'fibery/id',
        'enum/name'
    ] },

    { 'Cricket/Current Team': [
        'fibery/id',
        'Cricket/name'
    ] },

    { 'user/Former Teams': {
        'q/select': [
            'Cricket/name',
            'Cricket/Year Founded'
        ],
        'q/limit': 'q/no-limit'
    } },

    { 'oldest former team founded': [ 'q/min', ['user/Former Teams', 'Cricket/Year Founded'] ] }
  ],
  'q/limit': 2
});
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": [
                 "Cricket/Full Name",

                 { "Cricket/Batting Hand": [
                   "fibery/id",
                   "enum/name"
                 ] },

                 { "Cricket/Current Team": [
                   "fibery/id",
                   "Cricket/name"
                 ] },

                 { "user/Former Teams": {
                   "q/select": [
                     "Cricket/name",
                     "Cricket/Year Founded"
                   ],
                   "q/limit": "q/no-limit" }
                 },

                 { "oldest former team founded": [ "q/min", ["user/Former Teams", "Cricket/Year Founded"] ] }
               ],
               "q/limit": 2
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/Current Team": {
          "Cricket/name": "Delhi",
          "fibery/id": "d328b7b0-97fa-11e9-81b9-4363f716f666"
        },
        "Cricket/Batting Hand": {
          "enum/name": "Right",
          "fibery/id": "b0ed1370-9747-11e9-9f03-fd937c4ecf3b"
        },
        "Cricket/Full Name": "Virat 'Chikoo' Kohli",
        "user/Former Teams": [
          {
            "Cricket/name": "Delhi",
            "Cricket/Year Founded": 1934
          }
        ],
        "oldest former team founded": 1934
      },
      {
        "Cricket/Current Team": {
          "Cricket/name": "Sunrisers Hyderabad",
          "fibery/id": "2456d780-97fa-11e9-81b9-4363f716f666"
        },
        "Cricket/Batting Hand": {
          "enum/name": "Right",
          "fibery/id": "b0ed1370-9747-11e9-9f03-fd937c4ecf3b"
        },
        "Cricket/Full Name": "Kane Stuart Williamson",
        "user/Former Teams": [
          {
            "Cricket/name": "Northern Districts",
            "Cricket/Year Founded": 1955
          },
          {
            "Cricket/name": "Gloucestershire",
            "Cricket/Year Founded": 1870
          },
          {
            "Cricket/name": "Yorkshire",
            "Cricket/Year Founded": 1863
          },
          {
            "Cricket/name": "Barbados Tridents",
            "Cricket/Year Founded": 2013
          }
        ],
        "oldest former team founded": 1863
      }
    ]
  }
]
```

### Select aggregates

select-func is a Lisp-style function call

```
<select-func> = [<func>, <field-path>, ...]

<func> = "q/count" | "q/min" | "q/max" | ...
```

Available entity collection Field aggregates
* `q/count`
* `q/sum`
* `q/avg`
* `q/min`
* `q/max`

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#fba32f)
> It doesn't matter if a Field is populated manually or via a Formula/Lookup — the query stays exactly the same.

### Select rich text Field

Take a look how rich text Fields work in Fibery, if you haven't yet.

To select a rich text Field we should:

1. Get `fibery/secret` of the corresponding collaborative document.
2. Get the document via `api/documents` endpoint using this `fibery/secret`.

Supported document formats:
* Markdown (`md`) — default
* HTML (`html`)
* JSON of a particular structure (`json`)
* Plain-text (`plain-text`)

`Cricket/Player` Type used as an example

| Field name    | Field type                                     |
| ------------- | ---------------------------------------------- |
| `Cricket/Bio` | rich text (`Collaboration~Documents/Document`) |

Get the related collaborative documents `fibery/secret`:

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": [
                 "Cricket/name",
                 { "Cricket/Bio": [ "Collaboration~Documents/secret" ] }
               ],
               "q/limit": 2
             }
           }
         }
      ]'
```

Grab the secrets (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/name": "Virat Kohli",
        "Cricket/Bio": {
          "Collaboration~Documents/secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb"
        }
      },
      {
        "Cricket/name": "Kane Williamson",
        "Cricket/Bio": {
          "Collaboration~Documents/secret": "b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb"
        }
      }
    ]
  }
]
```

Get the documents one-by-one:

```
curl -X GET https://YOUR_ACCOUNT.fibery.io/api/documents/b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb?format=html \
     -H 'Authorization: Token YOUR_TOKEN' \

curl -X GET https://YOUR_ACCOUNT.fibery.io/api/documents/b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb?format=html \
     -H 'Authorization: Token YOUR_TOKEN' \
```

Result:

```
{
  "secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb",
  "content": "<p>Virat Kohli (born 5 November 1988) is an Indian <a href=\"https://en.wikipedia.org/wiki/Cricket\">cricketer</a> who currently captains the India national team.\nHe plays for Royal Challengers Bangalore in the Indian Premier League.</p>"
}

{
  "secret": "b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb",
  "content": "<p><strong>Kane Stuart Williamson</strong> (born 8 August 1990) is a New Zealand international <a href=\"https://en.wikipedia.org/wiki/Cricket\" title=\"Cricket\">cricketer</a> who is currently the <a href=\"https://en.wikipedia.org/wiki/Captain_(cricket)\" title=\"Captain (cricket)\">captain</a> of the <a href=\"https://en.wikipedia.org/wiki/New_Zealand_national_cricket_team\" title=\"New Zealand national cricket team\">New Zealand national team</a>.</p><p>He is a right-handed batsman and an occasional <a href=\"https://en.wikipedia.org/wiki/Off_spin\" title=\"Off spin\">off spin</a> bowler and is considered to be one of the best batsmen in the world.</p>"
}
```

Get multiple documents in a single batch request:

```
curl --location --request POST 'https://YOUR_ACCOUNT.fibery.io/api/documents/commands' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "command": "get-documents",
    "args": [
        {
            "secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb"
        },
        {
            "secret": "b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb"
        }
    ]
}'
```

Result:

```
[
    {
        "secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb",
        "content": "..."
    },
    {
        "secret": "b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb",
        "content": "..."
    }
]
```

### Filter Entities

Filters (where) go into the q/where clause of the query.

The general form is inspired by Lisp: it's a list where the first element is an operator and the remaining elements are the values to check using the operator:

```
<where> = [<operator> <operand> <operand> ...]

<operator> = ">", ">=", "<", "<=", ...
<operand> = <fieldexpr> | <subquery-vec>
```

In these examples we filter by:
* a primitive Field (height)
* two primitive Fields (birth date and retirement status)
* a single-select (batting hand)
* an entity Field (current team)
* an entity collection Field (former teams)

We don't compare Entity's Field to a value directly, but use a `$param` instead.

`Cricket/Player` Type used as an example

| Field name             | Field type              |
| ---------------------- | ----------------------- |
| `Cricket/Height`       | `fibery/decimal`        |
| `Cricket/Youth Career` | `fibery/date-range`     |
| `Cricket/Retired?`     | `fibery/bool`           |
| `Cricket/Batting Hand` | single-select           |
| `Cricket/Current Team` | entity Field            |
| `user/Former Teams`    | entity collection Field |

Operators
* `=`
* `!=`
* `<`
* `<=`
* `>`
* `>=`
* `q/contains`
* `q/not-contains`
* `q/in`
* `q/not-in`
* `q/and`
* `q/or`

Get players taller than 1.75 meters — primitive Field:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
   'q/from': 'Cricket/Player',
   'q/select': ['Cricket/name', 'Cricket/Height'],
   'q/where': ['>', ['Cricket/Height'], '$height' ],
   'q/limit': 2
}, { '$height': '1.75' });

```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": ["Cricket/name", "Cricket/Height"],
               "q/where": [">", ["Cricket/Height"], "$height" ],
               "q/limit": 2
             },
             "params": {
                "$height": "1.75"
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/name": "Cheteshwar Pujara",
        "Cricket/Height": "1.79"
      }
    ]
  }
]
```

Filters can be nested and combined using q/and and q/or. Here we are querying players who started their youth career before 2004 and haven't retired yet:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
  'q/from': 'Cricket/Player',
  'q/select': ['Cricket/name', 'Cricket/Youth Career', 'Cricket/Retired?'],
  'q/where': [
    'q/and',
    ['<', ['q/start', ['Cricket/Youth Career']], '$date'],
    ['=', ['Cricket/Retired?'], '$retired?']
  ],
  'q/limit': 2
}, {
  '$date': '2004-01-01',
  '$retired?': false
});
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": ["Cricket/name", "Cricket/Youth Career", "Cricket/Retired?"],
               "q/where": [
                 "q/and",
                 ["<", ["q/start", ["Cricket/Youth Career"]], "$date"],
                 ["=", ["Cricket/Retired?"], "$retired?"]
               ],
               "q/limit": 2
             },
             "params": {
               "$date": "2004-01-01",
               "$retired?": false
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/name": "Virat Kohli",
        "Cricket/Youth Career": {
          "start": "2002-10-01",
          "end": "2008-07-01"
        },
        "Cricket/Retired?": false
      }
    ]
  }
]
```

Get right-handed players — single-select:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
   'q/from': 'Cricket/Player',
   'q/select': ['Cricket/name', { 'Cricket/Batting Hand': ['enum/name'] }],
   'q/where': ['=', ['Cricket/Batting Hand', 'enum/name'], '$hand' ],
   'q/limit': 2
}, { '$hand': 'Right' });

```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": ["Cricket/name", { "Cricket/Batting Hand": ["enum/name"] } ],
               "q/where": ["=", ["Cricket/Batting Hand", "enum/name"], "$hand" ],
               "q/limit": 2
             },
             "params": {
               "$hand": "Right"
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/name": "Virat Kohli",
        "Cricket/Batting Hand": {
          "enum/name": "Right"
        }
      },
      {
        "Cricket/name": "Kane Williamson",
        "Cricket/Batting Hand": {
          "enum/name": "Right"
        }
      }
    ]
  }
]
```

Get players whose current team was founded before 2000 — entity Field:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
   'q/from': 'Cricket/Player',
   'q/select': ['Cricket/name', { 'Cricket/Current Team': ['Cricket/name'] }],
   'q/where': ['<', ['Cricket/Current Team', 'Cricket/Year Founded'], '$year' ],
   'q/limit': 2
}, { '$year': 2000 });

```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": ["Cricket/name", { "Cricket/Current Team": ["Cricket/name"] } ],
               "q/where": ["<", ["Cricket/Current Team", "Cricket/Year Founded"], "$year" ],
               "q/limit": 2
             },
             "params": {
               "$year": 2000
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/name": "Virat Kohli",
        "Cricket/Current Team": {
          "Cricket/name": "Delhi"
        }
      },
      {
        "Cricket/name": "Cheteshwar Pujara",
        "Cricket/Current Team": {
          "Cricket/name": "Saurashtra"
        }
      }
    ]
  }
]

```

Get players who previously played for Yorkshire or Derbyshire — entity collection Field:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
    'q/from': 'Cricket/Player',
    'q/select': ['Cricket/name', { 'user/Former Teams': { 'q/select': ['Cricket/name'], 'q/limit': 'q/no-limit' } } ],
    'q/where': ['q/in', ['user/Former Teams', 'Cricket/name'], '$teams' ],
    'q/limit': 2
}, { '$teams': ['Yorkshire', 'Derbyshire'] });
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": ["Cricket/name", { "user/Former Teams": { "q/select": ["Cricket/name"], "q/limit": "q/no-limit" } } ],
               "q/where": ["q/in", ["user/Former Teams", "Cricket/name"], "$teams" ],
               "q/limit": 2
             },
             "params": {
               "$teams": ["Yorkshire", "Derbyshire"]
             }
           }
         }
       ]'
```

Result (cURL):

```
[
    {
        "success": true,
        "result": [
            {
                "Cricket/name": "Kane Williamson",
                "user/Former Teams": [
                    { "Cricket/name": "Northern Districts" },
                    { "Cricket/name": "Gloucestershire" },
                    { "Cricket/name": "Yorkshire" },
                    { "Cricket/name": "Barbados Tridents" }
                ]
            },
            {
                "Cricket/name": "Cheteshwar Pujara",
                "user/Former Teams": [
                    { "Cricket/name": "Royal Challengers Bangalore" },
                    { "Cricket/name": "Yorkshire" },
                    { "Cricket/name": "Kolkata Knight Riders" },
                    { "Cricket/name": "Kings XI Punjab" },
                    { "Cricket/name": "Derbyshire" },
                    { "Cricket/name": "Nottinghamshire" }
                ]
            }
        ]
    }
]
```

### Order Entities

```
<order-by> = [[<field-path>, "q/asc" | "q/desc"], ...];
```

Sort Entities by multiple primitive and entity Fields.

The default sorting is by creation date and UUID:

`[ [["fibery/creation-date"], "q/asc"], [["fibery/id"], "q/asc"] ]`

Sorting by `fibery/id` guarantees that Entities order won't change on different executions of the same query.

`Cricket/Player` Type used as an example

| Field name             | Field type       |
| ---------------------- | ---------------- |
| `Cricket/Height`       | `fibery/decimal` |
| `Cricket/Current Team` | entity Field     |

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const players = await fibery.entity.query({
  'q/from': 'Cricket/Player',
  'q/select': [
    'Cricket/name',
    'Cricket/Height',
    { 'Cricket/Current Team': ['Cricket/name'] }
  ],
  'q/order-by': [
    [['Cricket/Height'], 'q/desc'],
    [['Cricket/Current Team', 'Cricket/name'], 'q/asc']
  ],
  'q/limit': 3
});
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": [
                 "Cricket/name",
                 "Cricket/Height",
                 { "Cricket/Current Team": ["Cricket/name"] }
               ],
               "q/order-by": [
                 [["Cricket/Height"], "q/desc"],
                 [["Cricket/Current Team", "Cricket/name"], "q/asc"]
               ],
               "q/limit": 3
             }
           }
         }
       ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": [
      {
        "Cricket/Current Team": {
          "Cricket/name": "Saurashtra"
        },
        "Cricket/Height": "1.79",
        "Cricket/name": "Cheteshwar Pujara"
      },
      {
        "Cricket/Current Team": {
          "Cricket/name": "Royal Challengers Bangalore"
        },
        "Cricket/Height": "1.75",
        "Cricket/name": "Virat Kohli"
      },
      {
        "Cricket/Current Team": {
          "Cricket/name": "Sunrisers Hyderabad"
        },
        "Cricket/Height": "1.75",
        "Cricket/name": "Kane Williamson"
      }
    ]
  }
]
```

### Create Entity

Create Entities with primitive, single-select and entity Fields.

Setting `fibery/id` is optional and might be useful for working with Entity right after creation.

To set a single-select or an entity Field we'll need the target Entity's `fibery/id`. We can get `fibery/id` either via API (check [Getting Entities](https://the.fibery.io/User_Guide/Guide/Entity-API-264/anchor=Get-Entities--0a5b17e3-bb53-4ee2-b14a-4e2757e1af9d "https://the.fibery.io/User_Guide/Guide/Entity-API-264/anchor=Get-Entities--0a5b17e3-bb53-4ee2-b14a-4e2757e1af9d"))or by opening the relevant Entity on UI and exploring the command response in browser's Network tab. 

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#9c2baf)
> Note that the target Entity should already exist.

Setting entity collection Fields on Entity creation is not supported. Instead we suggest updating entity collection Fields after the Entity is created.

Setting a rich text Field on creation is not possible either. Update rich text Field once the Entity is created instead.

`Cricket/Player` Type used as an example

| Field name             | Field type              |
| ---------------------- | ----------------------- |
| `fibery/id`            | `fibery/uuid`           |
| `fibery/public-id`     | `fibery/text`           |
| `Cricket/name`         | `fibery/text`           |
| `Cricket/Full Name`    | `fibery/text`           |
| `Cricket/Born`         | `fibery/date`           |
| `Cricket/Youth Career` | `fibery/date-range`     |
| `Cricket/Shirt Number` | `fibery/int`            |
| `Cricket/Height`       | `fibery/decimal`        |
| `Cricket/Retired?`     | `fibery/bool`           |
| `Cricket/Batting Hand` | single-select           |
| `Cricket/Current Team` | entity Field            |
| `user/Former Teams`    | entity collection Field |

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.entity.createBatch([
  {
    'type': 'Cricket/Player',
    'entity': {
      'fibery/id': 'd17390c4-98c8-11e9-a2a3-2a2ae2dbcce4',
      'Cricket/name': 'Curtly Ambrose',
      'Cricket/Full Name': 'Curtly Elconn Lynwall Ambrose',
      'Cricket/Born': '1963-09-21',
      'Cricket/Youth Career': {
        'start': '1985-01-01',
        'end': '1986-01-01'
      },
      'Cricket/Shirt Number': 1,
      'Cricket/Height': '2.01',
      'Cricket/Retired?': true,

      'Cricket/Batting Hand': { 'fibery/id': 'b0ed3a80-9747-11e9-9f03-fd937c4ecf3b' }
    }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/create",
           "args": {
             "type": "Cricket/Player",
             "entity": {
               "fibery/id": "d17390c4-98c8-11e9-a2a3-2a2ae2dbcce4",
               "Cricket/name": "Curtly Ambrose",
               "Cricket/Full Name": "Curtly Elconn Lynwall Ambrose",
               "Cricket/Born": "1963-09-21",
               "Cricket/Youth Career": {
                 "start": "1985-01-01",
                 "end": "1986-01-01"
               },
               "Cricket/Shirt Number": 1,
               "Cricket/Height": "2.01",
               "Cricket/Retired?": true,

               "Cricket/Batting Hand": { "fibery/id": "b0ed3a80-9747-11e9-9f03-fd937c4ecf3b" }
             }
           }
         }
       ]'
```

Result with all primitive Fields, single-selects and entity Fields:

```
[
  {
    "success": true,
    "result": {
      "Cricket/Height": "2.01",
      "fibery/modification-date": "2019-06-27T10:44:53.860Z",
      "Cricket/Born": "1963-09-21",
      "fibery/id": "98fd77a0-98c8-11e9-8af8-976831879f29",
      "fibery/creation-date": "2019-06-27T10:44:53.860Z",
      "Cricket/Shirt Number": 1,
      "Cricket/Full Name": "Curtly Elconn Lynwall Ambrose",
      "fibery/public-id": "6",
      "Cricket/Retired?": true,
      "Cricket/Current Team": null,
      "Cricket/Batting Hand": {
        "fibery/id": "b0ed3a80-9747-11e9-9f03-fd937c4ecf3b"
      },
      "Cricket/Youth Career": {
        "start": "1985-01-01",
        "end": "1986-01-01"
      },
      "Cricket/name": "Curtly Ambrose"
    }
  }
]
```

### Update Entity

Update primitive, single-select and entity Fields this way. For updating entity collection Fields check out the section below.

To update a single-select or an entity Field, we'll need the target Entity's `fibery/id`. We can get `fibery/id` either via API or by opening the relevant Entity on UI and exploring the command response in browser's Network tab. Note that the target Entity should already exist.

`Cricket/Player` Type used as an example

| Field name             | Field type              |
| ---------------------- | ----------------------- |
| `fibery/id`            | `fibery/uuid`           |
| `fibery/public-id`     | `fibery/text`           |
| `Cricket/name`         | `fibery/text`           |
| `Cricket/Full Name`    | `fibery/text`           |
| `Cricket/Born`         | `fibery/date`           |
| `Cricket/Youth Career` | `fibery/date-range`     |
| `Cricket/Shirt Number` | `fibery/int`            |
| `Cricket/Height`       | `fibery/decimal`        |
| `Cricket/Retired?`     | `fibery/bool`           |
| `Cricket/Batting Hand` | single-select           |
| `Cricket/Current Team` | entity Field            |
| `user/Former Teams`    | entity collection Field |

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.entity.updateBatch([
  {
    'type': 'Cricket/Player',
    'entity': {
      'fibery/id': '20f9b920-9752-11e9-81b9-4363f716f666',
      'Cricket/Full Name': 'Virat \"Chikoo\" Kohli',
      'Cricket/Current Team': { 'fibery/id': 'd328b7b0-97fa-11e9-81b9-4363f716f666' }
    }
  }
]);

```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/update",
           "args": {
             "type": "Cricket/Player",
             "entity": {
               "fibery/id": "20f9b920-9752-11e9-81b9-4363f716f666",
               "Cricket/Full Name": "Virat \"Chikoo\" Kohli",
               "Cricket/Current Team": { "fibery/id": "d328b7b0-97fa-11e9-81b9-4363f716f666" }
             }
           }
         }
       ]'
```

Result with all primitive Fields, single-select and entity Fields:

```
[
  {
    "success": true,
    "result": {
      "Cricket/Height": "1.75",
      "fibery/modification-date": "2019-06-27T12:17:02.842Z",
      "Cricket/Born": "1988-11-05",
      "fibery/id": "20f9b920-9752-11e9-81b9-4363f716f666",
      "fibery/creation-date": "2019-06-25T14:04:20.988Z",
      "Cricket/Shirt Number": 18,
      "Cricket/Full Name": "Virat \"Chikoo\" Kohli",
      "fibery/public-id": "1",
      "Cricket/Retired?": false,
      "Cricket/Current Team": {
        "fibery/id": "d328b7b0-97fa-11e9-81b9-4363f716f666"
      },
      "Cricket/Batting Hand": {
        "fibery/id": "b0ed1370-9747-11e9-9f03-fd937c4ecf3b"
      },
      "Cricket/Youth Career": {
        "start": "2002-10-01",
        "end": "2008-07-01"
      },
      "Cricket/name": "Virat Kohli"
    }
  }
]
```

#### Update entity collection Field

Add already existing Entities to an entity collection Field by providing their `fibery/id`. Remove Entities from the collection in a similar way.

Get `fibery/id` either via API or by opening the relevant Entity on UI and exploring the command response in browser's Network tab.

`Cricket/Player` Type used as an example

| Field name          | Field type              |
| ------------------- | ----------------------- |
| `fibery/id`         | `fibery/uuid`           |
| `user/Former Teams` | entity collection Field |

Add two existing Teams to Player's "Former Teams" entity collection Field:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.entity.addToEntityCollectionFieldBatch([
  {
    'type': 'Cricket/Player',
    'field': 'user/Former Teams',
    'entity': { 'fibery/id': '216c2a00-9752-11e9-81b9-4363f716f666' },
    'items': [
      { 'fibery/id': '0a3ae1c0-97fa-11e9-81b9-4363f716f666' },
      { 'fibery/id': '17af8db0-97fa-11e9-81b9-4363f716f666' }
    ]
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/add-collection-items",
           "args": {
             "type": "Cricket/Player",
             "field": "user/Former Teams",
             "entity": { "fibery/id": "216c2a00-9752-11e9-81b9-4363f716f666" },
             "items": [
               { "fibery/id": "0a3ae1c0-97fa-11e9-81b9-4363f716f666" },
               { "fibery/id": "17af8db0-97fa-11e9-81b9-4363f716f666" }
             ]
           }
         }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

Remove two Teams from Player's "Former Teams" entity collection Field:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.entity.removeFromEntityCollectionFieldBatch([
  {
    'type': 'Cricket/Player',
    'field': 'user/Former Teams',
    'entity': { 'fibery/id': '216c2a00-9752-11e9-81b9-4363f716f666' },
    'items': [
      { 'fibery/id': '0a3ae1c0-97fa-11e9-81b9-4363f716f666' },
      { 'fibery/id': '17af8db0-97fa-11e9-81b9-4363f716f666' }
    ]
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/remove-collection-items",
           "args": {
             "type": "Cricket/Player",
             "field": "user/Former Teams",
             "entity": { "fibery/id": "216c2a00-9752-11e9-81b9-4363f716f666" },
             "items": [
               { "fibery/id": "0a3ae1c0-97fa-11e9-81b9-4363f716f666" },
               { "fibery/id": "17af8db0-97fa-11e9-81b9-4363f716f666" }
             ]
           }
         }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

#### Update rich text Field

To update a rich text Field we should:

1. Get `fibery/secret` of the corresponding collaborative document.
2. Update the document via `api/documents` endpoint using this `fibery/secret`.

Supported document formats:
* Markdown (md) — default
* HTML (html)
* JSON of a particular structure (json)

`Cricket/Player` Type used as an example

| Field name    | Field type                                     |
| ------------- | ---------------------------------------------- |
| `Cricket/Bio` | rich text (`Collaboration~Documents/Document`) |

Get collaborative document's `fibery/secret`:

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/query",
           "args": {
             "query": {
               "q/from": "Cricket/Player",
               "q/select": [
                 "fibery/id",
                 { "Cricket/Bio": [ "Collaboration~Documents/secret" ] }
               ],
               "q/where": ["=", ["fibery/id"], "$id"],
               "q/limit": 1
             },
             "params": { "$id": "20f9b920-9752-11e9-81b9-4363f716f666" }
           }
         }
      ]'
```

Grab the secret:

```
[
  {
    "success": true,
    "result": [
      {
        "fibery/id": "20f9b920-9752-11e9-81b9-4363f716f666",
        "Cricket/Bio": {
          "Collaboration~Documents/secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb"
        }
      }
    ]
  }
]
```

Update the document:

```
curl -X PUT https://YOUR_ACCOUNT.fibery.io/api/documents/b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb?format=md \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "content": "Virat Kohli (born 5 November 1988) is an Indian [cricketer](https://en.wikipedia.org/wiki/Cricket) who currently captains the India national team.\nHe plays for Royal Challengers Bangalore in the Indian Premier League."
      }'

```

Update multiple documents in a single batch request:

```
curl -X POST 'https://YOUR_ACCOUNT.fibery.io/api/documents/commands?format=md' \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d \
      '{
         "command": "create-or-update-documents",
         "args": [
           {
             "secret": "b33a25d1-99ba-11e9-8c59-09d0cb6f3aeb",
             "content": "my md content 1"
           },
           {
             "secret": "b33a25d3-99ba-11e9-8c59-09d0cb6f3aeb",
             "content": "my md content 2"
           }
         ]
      }'

```

Status code 200 means that the update has been successful.

### Add comment

Once you install the Comments extension on a Type, you are free to add comments to the Type's Entities – both via UI and API.

Here at Fibery, we don't throw abstractions around so comments are assembled from the pre-existing basic building blocks:
* Comment (`comments/comment`) is a Type with Fields like Author (`comment/author`) and Creation Date (`fibery/creation-date`).
* The `Comments` extension connects a parent Type with Comment Type via a one-to-many relation.
* Each individual comment is an Entity of Comment Type.
* The content of a comment is stored in a collaborative document just like [rich-text Fields](https://the.fibery.io/User_Guide/Guide/Field-API-263/anchor=Rich-text-Field--a2a8947a-579b-4e7b-b9d1-a8ab7c2a9b4a "https://the.fibery.io/User_Guide/Guide/Field-API-263/anchor=Rich-text-Field--a2a8947a-579b-4e7b-b9d1-a8ab7c2a9b4a").

So here is how you add comment:

1. Create an Entity of the Comment Type.
2. Connect this comment to a proper parent Entity.
3. Set the comment's content.

Generate two UUIDs – for the comment ID and the document secret ID:

```
a88626cb-2f08-4821-9d5f-3edb9b624c26
9f18d395-05da-44dc-9f21-602b2e744b14
```

Create an Entity of the auxiliary Comment Type and link it to the parent Entity:

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

const PARENT_ENTITY_ID = '216c2a00-9752-11e9-81b9-4363f716f666';
const COMMENT_AUTHOR_ID = 'fe1db100-3779-11e9-9162-04d77e8d50cb';

const COMMENT_ID = 'a88626cb-2f08-4821-9d5f-3edb9b624c26'; // newly generated
const DOCUMENT_SECRET_ID = '9f18d395-05da-44dc-9f21-602b2e744b14'; // newly generated

const comment = await fibery.entity.create({
  'type': 'comments/comment',
  'entity': {
    'fibery/id': COMMENT_ID,
    'comment/document-secret': DOCUMENT_SECRET_ID,
    'comment/author': { 'fibery/id': COMMENT_AUTHOR_ID }
  }
});

await fibery.entity.addToEntityCollectionField({
    'type': 'Cricket/Player',
    'field': 'comments/comments',
    'entity': { 'fibery/id': PARENT_ENTITY_ID },
    'items': [
      { 'fibery/id': COMMENT_ID }
    ]
});

```

cURL

```
curl -X POST https://YO UR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
        {
          "command":"fibery.command/batch",
          "args":{
            "commands":[
              {
                "command":"fibery.entity/create",
                "args":{
                  "type":"comments/comment",
                  "entity":{
                    "fibery/id":"a88626cb-2f08-4821-9d5f-3edb9b624c26",
                    "comment/document-secret":"9f18d395-05da-44dc-9f21-602b2e744b14",
                    "comment/author": { "fibery/id": "fe1db100-3779-11e9-9162-04d77e8d50cb" }
                  }
                }
              },
              {
                "command":"fibery.entity/add-collection-items",
                "args":{
                  "type":"Cricket/Player",
                  "entity":{
                    "fibery/id":"20f9b920-9752-11e9-81b9-4363f716f666"
                  },
                  "field":"comments/comments",
                  "items":[
                    {
                      "fibery/id": "a88626cb-2f08-4821-9d5f-3edb9b624c26"
                    }
                  ]
                }
              }
            ]
          }
        }
      ]'
```

Make sure the result looks good:

```
[
  {
    "success": true,
    "result": [
      {
        "success": true,
        "result": {
          "comment/document-secret": "9f18d395-05da-44dc-9f21-602b2e744b14",
          "fibery/id": "a88626cb-2f08-4821-9d5f-3edb9b624c26",
          "fibery/public-id": "139",
          "fibery/creation-date": "2021-05-05T17:37:21.933Z",
          "comment/content": null,
          "comment/author": {
            "fibery/id": "fe1db100-3779-11e9-9162-04d77e8d50cb"
          }
        }
      },
      {
        "success": true,
        "result": null
      }
    ]
  }
]
```

Set the comment's content:

JavaScript

```
const content = 'He is the [G.O.A.T.](https://en.wikipedia.org/wiki/Greatest_of_All_Time) batsman!';
await fibery.document.update('9f18d395-05da-44dc-9f21-602b2e744b14', content, 'md');
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/documents/commands?format=md \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
         "command": "create-or-update-documents",
         "args": [
           {
             "secret": "9f18d395-05da-44dc-9f21-602b2e744b14",
             "content": "He is the [G.O.A.T.](https://en.wikipedia.org/wiki/Greatest_of_All_Time) batsman!"
           }
         ]
       }'
```

### Delete Entity

Delete Entity by providing its Type and `fibery/id`.

JavaScript

```
const Fibery = require('fibery-unofficial');
const fibery = new Fibery({host: "YOUR_ACCOUNT.fibery.io", token: YOUR_TOKEN});

await fibery.entity.deleteBatch([
  {
    'type': 'Cricket/Player',
    'entity': { 'fibery/id': 'b4f2e9b0-9907-11e9-acf1-fd0d502cdd20' }
  }
]);
```

cURL

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/commands \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '[
         {
           "command": "fibery.entity/delete",
           "args": {
             "type": "Cricket/Player",
             "entity": { "fibery/id": "93648510-9907-11e9-acf1-fd0d502cdd20" }
           }
         }
      ]'
```

Result (cURL):

```
[
  {
    "success": true,
    "result": "ok"
  }
]
```

## Views API

Views API is provided at `https://{YOUR_ACCOUNT}.fibery.io/api/views/json-rpc`.

It follows the [JSON-RPC specification](https://www.jsonrpc.org/specification).

### Getting views

To get a list of Views, use the `query-views` method.

All filters and params are optional. If omitted, all Views will be returned.

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/views/json-rpc \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "jsonrpc": "2.0",
        "method": "query-views",
        "params": {
          "filter": {
            "ids": ["b190008d-3fef-4df5-b8b9-1b432a0e0f05", "dd62b0df-537e-4c12-89f2-d937da128c7b"],
            "publicIds": ["1001", "1002"]
          }
        }
      }'

```

Possible filters are:

|             |                          |                                                                                                                                                                                               |
| ----------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`       | array of UUID strings    | Matches views by the `fibery/id` field.                                                                                                                                                       |
| `publicIds` | array of numeric strings | Matches views by the `fibery/public-id` field.                                                                                                                                                |
| `isPrivate` | `true` or `false`        | If true, return only matching views from "My space". If false, return only matching views outside of "My space". If omitted, matching views both from and outside of "My space" are returned. |
| `container` | {type: "entity";         |
 typeId: "6ded97e6-b4ca-4a8c-a740-6c34c3651cd1";
 publicIds: \["1", "2"\]} | If provided, the query will return only views attached to entities with the given public ids in the database (type) with the given typeId. |

### Creating views

To create one or more Views, use the `create-views` method:

"Container app" in this example contains a `fibery/id` reference to the space where the new View is to be created.

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/views/json-rpc \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "jsonrpc": "2.0",
        "method": "create-views",
        "params": {
          "views": [
            {
              "fibery/id": "3541bdf6-ab15-4d5e-b17b-eb124b8fe2f7",
              "fibery/name": "My Board",
              "fibery/type": "board",
              "fibery/meta": {},
              "fibery/container-app": {
                "fibery/id": "760ee2e2-e8ca-4f92-aaf2-4cde7f9dad0e"
              }
            }
          ]
        }
      }'
```

### Updating views

To update one or more Views, use the `update-views` method:

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/views/json-rpc \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "jsonrpc": "2.0",
        "method": "update-views",
        "params": {
          "updates": [
            {
              id: "3541bdf6-ab15-4d5e-b17b-eb124b8fe2f7",
              values: {
                "fibery/name": "My Updated Board",
                "fibery/meta": {},
              }
            }
          ]
        }
      }'

```

### Deleting views

To delete one or more Views, use the `delete-views` method:

```
curl -X POST https://YOUR_ACCOUNT.fibery.io/api/views/json-rpc \
     -H 'Authorization: Token YOUR_TOKEN' \
     -H 'Content-Type: application/json' \
     -d \
      '{
        "jsonrpc": "2.0",
        "method": "delete-views",
        "params": {
          "ids": ["3541bdf6-ab15-4d5e-b17b-eb124b8fe2f7"]
        }
      }'
```

## API FAQ

Here are some answers to the popular questions about API. If this page doesn't answer your question, please contact us in the support chat.

### How to create Single-Select and Multi-Select fields via Integration API?

Here are the prompts.

#### Single-select:

```
type: 'text',
subType: 'single-select'
```

#### Multi-select:

```
type: 'array[text]',
subType: 'multi-select',
```

#### Sample:

```
{
  state: {
      name: `State`,
      type: `text`,
      subType: `workflow`,
      options: [
          {
              name: `New`,
              default: true,
          },
          {name: `In Work`},
          {
              name: `Closed`,
              final: true,
          },
      ],
  },
}
```

> [//]: # (callout;icon-type=icon;icon=lightbulb-alt;color=#fba32f)
> Note, that if you want to update the values of the Multi-select, you need to treat that as a collection and use this guide - [addToEntityCollectionField](https://the.fibery.io/@public/User_Guide/Guide/Entity-API-264/anchor=Update-entity-collection-Field--ea6b2bd3-6085-41ed-abf8-77c81d627ba9)
>
> ```
> await fibery.entity.addToEntityCollectionField({
>     'type': 'Cricket/Player',
>     'field': 'comments/comments',
>     'entity': { 'fibery/id': PARENT_ENTITY_ID },
>     'items': [
>       { 'fibery/id': COMMENT_ID }
>     ]
> });
> ```

#### Workflow:

```
type: 'text',
subType: 'workflow`
```

Optionally you can pass a list of `options`. If the options property is missing, Fibery will try to identify options based on your data dynamically.

#### Options format:

```
[
  {
     name: 'Open', 
     color: '#123414', // OPTIONAL
     default: true/false,  // Workflow should have record with default flag
     final: true/false // workflow final step
   }
]
```

> [//]: # (callout;icon-type=icon;icon=exclamation-circle;color=#1fbed3)
>  It’s also possible to pass multi-select with type `text` but in this case, options should be comma-separated (e.g. `dev,high prio,r22`)

### How can I create a Muli Select using the API?

It’s maybe not clear from the documentation, but select fields (single- and multi-selects) are basically databases, where each entity is an option, and there is a relation (many-to-one or many-to-many) from the main database to the select db.\
So to create a select field, you have to create an `enum db` and then create a field in your main db that is a relation to it.\
See [here](https://the.fibery.io/@public/User_Guide/Guide/Field-API-263/anchor=Relation-\(entity-collection-Field\)--a3c35d51-339b-4d06-bd70-45fc441e65ae) for some helpful info.

### Is there a way to see logs and print out something in Script Actions (Execute Javascript Code)?

Please use `console.log()` in js code, and it's output will be available in the Button/Rule Activity Log

### How to call the Location field via API?

#### GraphQL

Unfortunately, not possible at the moment. 

#### REST API

The location field should work like any other field, both in regular / HTTP API and in javascript API in automations. 

![image.png](https://the.fibery.io/api/files/0615462e-0bd7-43b8-b5d8-5f03578b927d#width=1788&height=1170 "")

### How to update the avatar with a URL to an image?

Avatars is the same file collection as the files, so check [[User Guide/Guide: File API#^dee06c51-f937-11ec-aafd-7332cdf16307/ce14f0d0-b146-11ee-80ca-873024c45f1c]] 

You can find a [nice discussion in our community ](https://community.fibery.io/t/manipulating-the-avatar-via-automation-script/3918 "https://community.fibery.io/t/manipulating-the-avatar-via-automation-script/3918")🙂 

### How to update the Icon Field?

```
await fibery.updateEntity(entity.type, entity.id, {'Icon': ':grimacing:'});
```

### How to work with the Lookup Field?

A Lookup Field is basically the same as a Formula field.

Feel free to share your use case in [the community](https://the.fibery.io/User_Guide/Guide/Entity-API-264/anchor=Get-Entities--0a5b17e3-bb53-4ee2-b14a-4e2757e1af9d "https://the.fibery.io/User_Guide/Guide/Entity-API-264/anchor=Get-Entities--0a5b17e3-bb53-4ee2-b14a-4e2757e1af9d").

### How to work with Documents?

This API is still undocumented. However, to work with Document View content using ordinary or api documents, you need only the document secret.

To obtain that secret for a document view with public id "45" one may query views api as described here - [[User Guide/Guide: View API#^dee06c51-f937-11ec-aafd-7332cdf16307/f9f5bd50-b147-11ee-a835-fddaae4c80e5]] 

```
{
  "jsonrpc": "2.0",
  "method": "query-views",
  "params": {
    "filter": {
      "publicIds": ["45"]
    }
  }
}
```

Response

```
{
  "jsonrpc": "2.0",
  "result": [
    {
      "fibery/id": "43addb30-1fd0-11ee-9009-a7c752e861c6",
      "fibery/public-id": "45",
      "fibery/name": "Supa Doc",
      "fibery/icon": null,
      "fibery/description": null,
      "fibery/rank": -9006999178042705,
      "fibery/type": "document",
      "fibery/meta": {
          "documentSecret": "e27df257-0e6f-441f-8dcc-fde2591d12c3"
      },
      ...
    }
  ]
}
```

See the `"fibery/meta"` property with `"documentSecret"` in it. With this UUID you may do whatever you need with document content via standard documents API.

### API Token Activity Details 

You can see the "Created" and "Last Used" dates for API tokens, along with the token prefix. For older tokens, the creation date won’t be available and will show as "N/A." Activity tracking (last used date) will also be shown from September 19th, 2024.

### Troubleshooting

#### I'm trying to connect to my PostgresQL database and get "Server is not available... Caused by: SSL/TLS required" error

You can use `?ssl=true` to fix the issue. Find the example reference in [this community thread](https://community.render.com/t/ssl-tls-required/1022/3 "https://community.render.com/t/ssl-tls-required/1022/3"). 

#### I have error "Version is required"

Please, check you config.app.json file

The config must contain the following keys:

```
[
    `name`,
    `version`,
    `authentication`,
    `sources`,
    `description`,
]
```

#### I'm facing timeouts

We recommend dividing your entities into separate batches that are processed individually by different Rules, all of which perform the same operation but on distinct subsets of entities.

The downside is that you now need to maintain multiple Rules instead of one.

[Here](https://community.fibery.io/t/7506) you can check our community discussion and vote for potential improvements. You are also welcome to check  [Fibery Script Management tool](https://community.fibery.io/t/beta-testers-wanted-for-fibery-script-management-tool/5466) written by our partner Matt – so you could write and maintain a single script that could be automatically pushed to multiple Rules.

#### I have problem "\[Violation\] 'SetTimeout' handler"

This error is not related directly to the rule. Maybe it was caused by something else (e.g. a browser extension).

We don't write `console.log` statements from a script to the browser console when executing rules.

It's impossible, as the rule is run automatically, not triggered by a user. For buttons, we do this.

What you can do right now:
* Check the outputs of `console.log` statements in the rule's Activity Log.
* Add steps to the scripts as described in the [debugging](https://the.fibery.io/@public/User_Guide/Guide/Scripts-in-Automations-54/anchor=Debugging--a77fbd4d-dc37-489f-9f46-00d8294a1f47) part.