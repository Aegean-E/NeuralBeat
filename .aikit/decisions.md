# Decisions

Why this project is built the way it is, oldest first. One entry per decision that changes a
contract, a dependency, a data format or the architecture; IDs are consecutive and never reused.

<!-- Entry format:
### ADR-NNN: <decision in one line>
- **Date**: YYYY-MM-DD
- **Status**: Accepted
- **Context**: <what forced the decision>
- **Decision**: <what was decided>
- **Consequences**: <what follows, including what it costs>
-->

### ADR-001: Relicense NeuralBeat to AGPL-3.0
- **Date**: 2026-10-20
- **Status**: Accepted
- **Context**: NeuralBeat shipped under Apache-2.0 while the rest of the project portfolio moved to AGPL-3.0, so the repository, README and GitHub license badge disagreed with the portfolio contract.
- **Decision**: Replace the Apache-2.0 LICENSE with the canonical GNU Affero General Public License v3.0 text, update the README license section, and publish the change with the repository.
- **Consequences**:
  - *Positive*: One copyleft contract across the portfolio; GitHub detects AGPL-3.0; contributors and users see the same terms in LICENSE and README.
  - *Trade-offs*: NeuralBeat moves from a permissive license to a strong copyleft license; consumers who need Apache-2.0 terms must use an earlier commit or request a separate grant.
- Cross-principle check: PRINCIPLE-005 (README), PRINCIPLE-016 (ADR), PRINCIPLE-018 (commit and push).
