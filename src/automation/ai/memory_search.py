from __future__ import annotations

from typing import Any

from nltk.corpus import stopwords


class MemorySearch:
    """
    Search utility for AI memory.
    """

    def find(
        self,
        data: dict[str, Any],
        key: str,
        default=None,
    ):
        return data.get(
            key,
            default,
        )

    # -------------------------------- #

    def exists(
        self,
        data: dict[str, Any],
        key: str,
    ) -> bool:
        return key in data

    # -------------------------------- #

    def keys(
        self,
        data: dict[str, Any],
    ):
        return list(
            data.keys()
        )

    # -------------------------------- #

    def values(
        self,
        data: dict[str, Any],
    ):
        return list(
            data.values()
        )

    # -------------------------------- #

    def search(
        self,
        data: dict[str, Any],
        keyword: str,
    ) -> dict[str, Any]:

        keyword = keyword.lower()

        result = {}

        for key, value in data.items():

            if keyword in key.lower():
                result[key] = value

                continue

            if keyword in str(value).lower():
                result[key] = value

        return result

    # -------------------------------- #

    def search_conversation(
        self,
        data: dict[str, Any],
        query: str,
    ) -> list[dict[str, Any]]:

        query = query.lower().strip()

        if not query:
            return []

        stop_words = set(
            stopwords.words("english")
        )

        # -------------------------------- #
        # Extract meaningful query words
        # -------------------------------- #

        query_words = {
            word.strip(".,!?;:")
            for word in query.split()
            if word.strip(".,!?;:")
            and word.strip(".,!?;:") not in stop_words
        }

        if not query_words:
            return []

        results = []

        # -------------------------------- #
        # Search conversation memories
        # -------------------------------- #

        for value in data.values():

            if not isinstance(value, dict):
                continue

            if value.get("type") != "conversation":
                continue

            content = str(
                value.get("content", "")
            ).lower()

            content_words = {
                word.strip(".,!?;:")
                for word in content.split()
                if word.strip(".,!?;:")
            }

            matched_words = (
                query_words & content_words
            )

            if matched_words:

                result = dict(value)

                result["_match_score"] = len(
                    matched_words
                )

                results.append(result)

        # -------------------------------- #
        # Rank results
        # -------------------------------- #

        results.sort(
            key=lambda memory: (
                memory.get("_match_score", 0),
                memory.get("importance", 0),
            ),
            reverse=True,
        )

        # -------------------------------- #
        # Remove internal score
        # -------------------------------- #

        for memory in results:
            memory.pop(
                "_match_score",
                None,
            )

        return results

    # -------------------------------- #

    def __repr__(self):
        return "<MemorySearch>"