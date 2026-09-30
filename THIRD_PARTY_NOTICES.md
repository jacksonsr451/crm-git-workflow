# Third-Party Notices

The project may use libraries, frameworks, fonts, assets, APIs, and other components provided by third parties. Those materials may be subject to their own copyright notices, licenses, attribution requirements, patent terms, or other conditions.

The proprietary license for this project does not replace, relicense, or override licenses applicable to third-party materials. The project license and dependency licenses must be considered separately. A dependency being included in the project does not make the project open source, and the project's proprietary terms do not remove rights required by a third-party license.

## Notice strategy

Before a release or external distribution:

1. inventory direct and transitive dependencies actually shipped or used;
2. identify the license and notice requirements for each dependency;
3. distinguish runtime, development-only, generated, bundled, and optional components;
4. validate compatibility with the intended proprietary distribution model;
5. generate a reviewed notices artifact from the locked dependency manifests; and
6. include required notices and preserve source/license references where required.

The tool, format, review owner, release gate, and dependency manifests are `TBD` because implementation has not started. Do not copy an entire dependency tree into this file manually. This document is a policy placeholder, not a complete notice inventory.
