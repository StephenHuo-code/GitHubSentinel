# Langchain-AI/Langchain Daily Progress Report for 2024-09-07 

## Issues Summary

1. Updates requested for Google BigQuery Vector Search documentation with a new SQL filter feature introduced in *langchain-google-community 1.0.9* (#26184, #26183).
2. Session expiry issues experienced with neo4j graph (#26182).
3. BoxRetriever needs added search options and documentation as an agent tool (#26181).
4. Dependency problems identified in rag tutorial (#26174).
5. Clarification requested about units for threshold amount (#26171).
6. The function as_retriever() of DatabricksVectorSearch class has unexpected keyword argument 'query_type' (#26170).
7. ChatOctoAI needs the bind_tools feature (#26168).
8. LC Academy links were suggested to be added to the documentations (#26164).
9. Infinite call issue for llamafile reported (#26160).
10. Embbeding namespaces need protection in langchain community patch (#26156).

Several more issues relating to features and functionality, including JSON support in ChatGoogleGenerativeAI, bugs in UnstructuredPDFLoader and Azure Cosmos DB, and requests for multi-tenant support for caching, the addition of siliconflow-based LLM implementation and custom LLM bind_tools feature usage.

## Pull Requests Summary

1. Updated Google BigQuery Vector Search documentation with a new SQL filter feature introduced in *langchain-google-community 1.0.9* (#26184).
2. Added session expired retry to neo4j graph (#26182).
3. Added search options and wrote documentation for BoxRetriever as an agent tool (#26181). 
4. Rag tutorial dependencies were updated (#26174).
5. Added the tools binding in ChatOctoAI (#26168).
6. LC Academy links were added to the documentations (#26164).

More pull requests were made regarding documentation and updates, integration of the siliconflow-based LLM, connectivity improvements, addition of HuggingFacePipeline model_id parameter, various fixations for bugs and issues, and support for Bedrock cross-region inference models.