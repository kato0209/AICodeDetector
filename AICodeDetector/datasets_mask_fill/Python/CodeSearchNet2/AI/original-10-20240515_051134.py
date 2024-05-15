
        return self.session.query(models.Health).filter(
            models.Health.dag_id == self.dag_id,
            models.Health.state == 'healthy',
            models.Health.latest_heartbeat < (timezone.utcnow() - timedelta(
                minutes=5)
            ),
        ).count() > 0


class Pool(Base):
    __tablename__ = "slot_pool"

    id = Column(Integer, primary_key=True)
    pool = Column(String(50), unique=True)
    slots = Column(Integer, default=0)
    description = Column(